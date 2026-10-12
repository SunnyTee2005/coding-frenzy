//! 偵測本機的編譯器 / 直譯器。
//!
//! macOS 的 `/usr/bin/clang`、`/usr/bin/python3` 等在沒裝 Xcode Command Line Tools 時
//! 只是佔位程式，一執行就會跳出安裝視窗。所以要先用 `xcode-select -p` 確認 CLT
//! 已安裝，才把 `/usr/bin` 底下的工具視為可用。

use crate::Language;
use serde::Serialize;
use std::path::{Path, PathBuf};
use std::process::Command;

#[derive(Debug, Clone, Serialize)]
pub struct ToolStatus {
    pub lang_id: String,
    pub display: String,
    pub program: Option<PathBuf>,
    pub version: Option<String>,
}

/// 從 Finder / Dock 啟動的 App 拿到的 PATH 只有 `/usr/bin:/bin:/usr/sbin:/sbin`，
/// 補上常見的安裝位置。
pub fn default_extra_paths() -> Vec<PathBuf> {
    let mut v = Vec::new();
    if cfg!(target_os = "macos") {
        v.push(PathBuf::from("/opt/homebrew/bin"));
        v.push(PathBuf::from("/usr/local/bin"));
    }
    v
}

/// 找出這個語言第一個可用的執行檔。
pub fn resolve(lang: &Language, extra_paths: &[PathBuf]) -> Option<PathBuf> {
    lang.programs.iter().find_map(|name| which(name, extra_paths))
}

/// 在 PATH（加上 `extra_paths`）中尋找執行檔。
pub fn which(name: &str, extra_paths: &[PathBuf]) -> Option<PathBuf> {
    let path_var = std::env::var_os("PATH").unwrap_or_default();
    let dirs = std::env::split_paths(&path_var).chain(extra_paths.iter().cloned());
    for dir in dirs {
        for candidate in candidates(&dir, name) {
            if candidate.is_file() && usable(&candidate) {
                return Some(candidate);
            }
        }
    }
    None
}

fn candidates(dir: &Path, name: &str) -> Vec<PathBuf> {
    if cfg!(windows) {
        vec![dir.join(format!("{name}.exe")), dir.join(name)]
    } else {
        vec![dir.join(name)]
    }
}

#[cfg(target_os = "macos")]
fn usable(path: &Path) -> bool {
    // /usr/bin 的開發工具在沒有 CLT 時是會跳安裝視窗的佔位程式。
    !path.starts_with("/usr/bin") || command_line_tools_installed()
}

#[cfg(windows)]
fn usable(path: &Path) -> bool {
    // WindowsApps 底下的 python.exe 是開啟 Microsoft Store 的捷徑，不是真的 Python。
    !path.to_string_lossy().to_ascii_lowercase().contains("windowsapps")
}

#[cfg(not(any(target_os = "macos", windows)))]
fn usable(_path: &Path) -> bool {
    true
}

/// macOS：Xcode Command Line Tools 是否已安裝。其他平台恆為 true。
pub fn command_line_tools_installed() -> bool {
    if !cfg!(target_os = "macos") {
        return true;
    }
    Command::new("/usr/bin/xcode-select")
        .arg("-p")
        .output()
        .map(|o| o.status.success())
        .unwrap_or(false)
}

/// macOS：叫出系統的「安裝命令列開發者工具」視窗。安裝在背景進行，
/// 呼叫端應輪詢 [`command_line_tools_installed`]。
pub fn request_command_line_tools_install() -> std::io::Result<()> {
    if cfg!(target_os = "macos") {
        // 已安裝或安裝視窗已開著時會回傳非 0，這裡不視為錯誤。
        Command::new("/usr/bin/xcode-select").arg("--install").status()?;
    }
    Ok(())
}

/// 列出每個語言是否可用與版本。
pub fn detect(langs: &[Language], extra_paths: &[PathBuf]) -> Vec<ToolStatus> {
    langs
        .iter()
        .map(|lang| {
            let program = resolve(lang, extra_paths);
            let version = program.as_deref().and_then(version_of);
            ToolStatus { lang_id: lang.id.clone(), display: lang.display.clone(), program, version }
        })
        .collect()
}

fn version_of(program: &Path) -> Option<String> {
    let out = Command::new(program).arg("--version").output().ok()?;
    let text = if out.stdout.is_empty() { out.stderr } else { out.stdout };
    String::from_utf8_lossy(&text).lines().next().map(|l| l.trim().to_string()).filter(|l| !l.is_empty())
}
