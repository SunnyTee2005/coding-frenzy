//! 執行子行程：stdin 從檔案讀、stdout / stderr 寫到檔案（避免管線塞住），
//! 並強制牆鐘時間與輸出大小上限。
//!
//! Unix（macOS / Linux）：子行程放進自己的 process group，逾時時整組 SIGKILL；
//! 以 `RLIMIT_CPU` 再加一道 CPU 時間保險；用 `wait4` 取得 CPU 時間與最大記憶體。
//! Windows：目前只做逾時強制結束，Phase 5 改用 Job Object。

use serde::Serialize;
use std::fs::File;
use std::io;
use std::path::Path;
use std::process::{Command, Stdio};
use std::time::{Duration, Instant};

#[derive(Debug, Clone)]
pub struct ProcLimits {
    /// 牆鐘時間上限，超過就強制結束。
    pub wall: Duration,
    /// stdout 大小上限（bytes）。
    pub output_bytes: u64,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize)]
pub enum ProcStatus {
    Exited(i32),
    Signaled(i32),
    TimedOut,
    OutputLimit,
}

#[derive(Debug, Clone)]
pub struct ProcOutcome {
    pub status: ProcStatus,
    pub stdout: Vec<u8>,
    pub stderr: Vec<u8>,
    pub elapsed: Duration,
    /// 被 RLIMIT_CPU 終止（SIGXCPU）。
    pub cpu_exceeded: bool,
    pub max_rss_kb: Option<u64>,
}

pub fn run(argv: &[String], cwd: &Path, stdin: Option<&Path>, limits: &ProcLimits) -> io::Result<ProcOutcome> {
    let io_dir = tempfile::Builder::new().prefix("cpe-io-").tempdir()?;
    let out_path = io_dir.path().join("stdout");
    let err_path = io_dir.path().join("stderr");

    let mut cmd = Command::new(&argv[0]);
    cmd.args(&argv[1..])
        .current_dir(cwd)
        .stdin(match stdin {
            Some(p) => Stdio::from(File::open(p)?),
            None => Stdio::null(),
        })
        .stdout(File::create(&out_path)?)
        .stderr(File::create(&err_path)?);
    platform::configure(&mut cmd, limits);

    let start = Instant::now();
    let child = cmd.spawn()?;
    let (status, cpu_exceeded, max_rss_kb) = platform::wait(child, start, limits, &out_path)?;
    let elapsed = start.elapsed();

    Ok(ProcOutcome {
        status,
        stdout: std::fs::read(&out_path)?,
        stderr: std::fs::read(&err_path)?,
        elapsed,
        cpu_exceeded,
        max_rss_kb,
    })
}

/// 輪詢間隔：剛開始密集一點，讓短程式的時間量得準。
fn poll_interval(since_start: Duration) -> Duration {
    if since_start < Duration::from_millis(100) {
        Duration::from_millis(1)
    } else {
        Duration::from_millis(10)
    }
}

fn output_too_large(path: &Path, limit: u64) -> bool {
    std::fs::metadata(path).map(|m| m.len() > limit).unwrap_or(false)
}

#[cfg(unix)]
mod platform {
    use super::*;
    use std::os::unix::process::CommandExt;

    pub fn configure(cmd: &mut Command, limits: &ProcLimits) {
        let cpu_secs = limits.wall.as_secs() + 1;
        unsafe {
            cmd.pre_exec(move || {
                if libc::setpgid(0, 0) != 0 {
                    return Err(io::Error::last_os_error());
                }
                let cpu = libc::rlimit { rlim_cur: cpu_secs as libc::rlim_t, rlim_max: (cpu_secs + 1) as libc::rlim_t };
                libc::setrlimit(libc::RLIMIT_CPU, &cpu);
                let core = libc::rlimit { rlim_cur: 0, rlim_max: 0 };
                libc::setrlimit(libc::RLIMIT_CORE, &core);
                Ok(())
            });
        }
    }

    pub fn wait(
        child: std::process::Child,
        start: Instant,
        limits: &ProcLimits,
        out_path: &Path,
    ) -> io::Result<(ProcStatus, bool, Option<u64>)> {
        let pid = child.id() as libc::pid_t;
        let mut forced: Option<ProcStatus> = None;
        loop {
            let mut status: libc::c_int = 0;
            let mut usage: libc::rusage = unsafe { std::mem::zeroed() };
            let r = unsafe { libc::wait4(pid, &mut status, libc::WNOHANG, &mut usage) };
            if r == -1 {
                let err = io::Error::last_os_error();
                if err.kind() == io::ErrorKind::Interrupted {
                    continue;
                }
                kill_group(pid);
                return Err(err);
            }
            if r == pid {
                // 主行程結束後，把它可能留下的子孫行程一起清掉。
                kill_group(pid);
                let max_rss_kb = max_rss_kb(&usage);
                if let Some(s) = forced {
                    return Ok((s, false, max_rss_kb));
                }
                if libc::WIFEXITED(status) {
                    return Ok((ProcStatus::Exited(libc::WEXITSTATUS(status)), false, max_rss_kb));
                }
                let sig = libc::WTERMSIG(status);
                return Ok((ProcStatus::Signaled(sig), sig == libc::SIGXCPU, max_rss_kb));
            }
            if forced.is_none() {
                if start.elapsed() > limits.wall {
                    forced = Some(ProcStatus::TimedOut);
                } else if output_too_large(out_path, limits.output_bytes) {
                    forced = Some(ProcStatus::OutputLimit);
                }
                if forced.is_some() {
                    kill_group(pid);
                    continue;
                }
            }
            std::thread::sleep(poll_interval(start.elapsed()));
        }
    }

    fn kill_group(pid: libc::pid_t) {
        unsafe {
            libc::kill(-pid, libc::SIGKILL);
        }
    }

    fn max_rss_kb(usage: &libc::rusage) -> Option<u64> {
        let rss = usage.ru_maxrss as u64;
        // macOS 的 ru_maxrss 單位是 bytes，Linux 是 KB。
        Some(if cfg!(target_os = "macos") { rss / 1024 } else { rss })
    }
}

#[cfg(not(unix))]
mod platform {
    use super::*;

    pub fn configure(cmd: &mut Command, _limits: &ProcLimits) {
        #[cfg(windows)]
        {
            use std::os::windows::process::CommandExt;
            const CREATE_NO_WINDOW: u32 = 0x0800_0000;
            cmd.creation_flags(CREATE_NO_WINDOW);
        }
    }

    pub fn wait(
        mut child: std::process::Child,
        start: Instant,
        limits: &ProcLimits,
        out_path: &Path,
    ) -> io::Result<(ProcStatus, bool, Option<u64>)> {
        loop {
            if let Some(status) = child.try_wait()? {
                return Ok((ProcStatus::Exited(status.code().unwrap_or(-1)), false, None));
            }
            let forced = if start.elapsed() > limits.wall {
                Some(ProcStatus::TimedOut)
            } else if output_too_large(out_path, limits.output_bytes) {
                Some(ProcStatus::OutputLimit)
            } else {
                None
            };
            if let Some(s) = forced {
                let _ = child.kill();
                let _ = child.wait();
                return Ok((s, false, None));
            }
            std::thread::sleep(poll_interval(start.elapsed()));
        }
    }
}
