//! 題庫格式：
//!
//! ```text
//! problems/uva-10055/
//!   meta.toml        id、題名、星等、時限、UVa 編號
//!   statement.md     自行改寫的題目敘述
//!   sample/  1.in 1.out ...   題目預設測試資料（題目上的範例）
//!   public/  1.in 1.out ...   人工公開測試資料
//!   hidden/  1.in 1.out ...   正式評判用的暗中測試資料
//!   sol.cpp          標準解（產生與驗證測資用）
//! ```

use serde::{Deserialize, Serialize};
use std::io;
use std::path::{Path, PathBuf};
use std::time::Duration;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ProblemMeta {
    pub id: String,
    pub title: String,
    pub stars: u8,
    /// 秒。
    #[serde(default = "default_time_limit")]
    pub time_limit: f64,
    #[serde(default)]
    pub uva: Option<u32>,
}

// TODO(Phase 0)：確認考場的預設時限。
fn default_time_limit() -> f64 {
    3.0
}

#[derive(Debug, Clone, Serialize)]
pub struct Problem {
    pub meta: ProblemMeta,
    pub statement: String,
    #[serde(skip)]
    pub dir: PathBuf,
}

impl Problem {
    pub fn time_limit(&self) -> Duration {
        Duration::from_secs_f64(self.meta.time_limit)
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum TestSet {
    Sample,
    Public,
    Hidden,
}

impl TestSet {
    pub const ALL: [TestSet; 3] = [TestSet::Sample, TestSet::Public, TestSet::Hidden];

    pub fn dir_name(self) -> &'static str {
        match self {
            TestSet::Sample => "sample",
            TestSet::Public => "public",
            TestSet::Hidden => "hidden",
        }
    }
}

#[derive(Debug, Clone, Serialize)]
pub struct TestCase {
    pub name: String,
    #[serde(skip)]
    pub input: Vec<u8>,
    #[serde(skip)]
    pub output: Vec<u8>,
}

pub fn load_problem(dir: &Path) -> io::Result<Problem> {
    let meta_text = std::fs::read_to_string(dir.join("meta.toml"))?;
    let meta: ProblemMeta = toml::from_str(&meta_text)
        .map_err(|e| io::Error::new(io::ErrorKind::InvalidData, format!("{}: {e}", dir.display())))?;
    let statement = std::fs::read_to_string(dir.join("statement.md")).unwrap_or_default();
    Ok(Problem { meta, statement, dir: dir.to_path_buf() })
}

/// 讀取題庫根目錄下所有題目（有 `meta.toml` 的子目錄），依 id 排序。
pub fn list_problems(root: &Path) -> io::Result<Vec<Problem>> {
    let mut problems = Vec::new();
    for entry in std::fs::read_dir(root)? {
        let path = entry?.path();
        if path.join("meta.toml").is_file() {
            problems.push(load_problem(&path)?);
        }
    }
    problems.sort_by_key(|p| natural_key(&p.meta.id));
    Ok(problems)
}

/// 讀取一組測資；目錄不存在時回傳空清單。`N.in` 需有對應的 `N.out`。
pub fn load_tests(problem: &Problem, set: TestSet) -> io::Result<Vec<TestCase>> {
    let dir = problem.dir.join(set.dir_name());
    if !dir.is_dir() {
        return Ok(Vec::new());
    }
    let mut names: Vec<String> = std::fs::read_dir(&dir)?
        .filter_map(|e| e.ok())
        .filter_map(|e| {
            let name = e.file_name().into_string().ok()?;
            name.strip_suffix(".in").map(str::to_string)
        })
        .collect();
    names.sort_by_key(|n| natural_key(n));
    names
        .into_iter()
        .map(|name| {
            let input = std::fs::read(dir.join(format!("{name}.in")))?;
            let output = std::fs::read(dir.join(format!("{name}.out"))).map_err(|e| {
                io::Error::new(e.kind(), format!("{}/{name}.out：{e}", dir.display()))
            })?;
            Ok(TestCase { name: format!("{}/{name}", set.dir_name()), input, output })
        })
        .collect()
}

/// 讓 "2" 排在 "10" 前面。
fn natural_key(s: &str) -> (u64, String) {
    let digits: String = s.chars().filter(char::is_ascii_digit).collect();
    (digits.parse().unwrap_or(u64::MAX), s.to_string())
}
