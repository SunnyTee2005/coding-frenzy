//! 考試狀態：所有視窗（主畫面、各題的解題視窗、成績表）共用同一份，存在 app data 目錄，
//! App 當掉或關閉後可以接續。前端透過 command 讀寫，變動後由 lib.rs 廣播 `session-changed`。
//!
//! 這個模組不依賴 Tauri，方便單元測試。

use cpe_judge::Verdict;
use serde::{Deserialize, Serialize};
use std::collections::BTreeMap;
use std::io;
use std::path::{Path, PathBuf};
use std::time::{SystemTime, UNIX_EPOCH};

pub fn now_ms() -> u64 {
    SystemTime::now().duration_since(UNIX_EPOCH).map(|d| d.as_millis() as u64).unwrap_or(0)
}

/// 主畫面目前在哪個階段。
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize, Default)]
#[serde(rename_all = "camelCase")]
pub enum Phase {
    /// 授權規定頁。
    #[default]
    License,
    /// 已同意授權，等待登入。
    Login,
    /// 已登入、考試進行中（或已結束，見 `Exam::ended_at_ms`）。
    Exam,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Examinee {
    /// (A) 身分證字號或護照號碼
    pub id_no: String,
    /// (B) 姓名
    pub name: String,
    /// (C) 准考碼
    pub ticket: String,
    /// (D) 認證碼
    pub auth_code: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ExamProblem {
    /// 題號，例如 `00A1`。
    pub label: String,
    pub problem_id: String,
}

/// 一次正式評判。
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Submission {
    pub problem_id: String,
    pub at_ms: u64,
    /// 從開考起算的整數分鐘（無條件捨去），計分用。
    pub minute: u64,
    pub verdict: Verdict,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Exam {
    pub code: String,
    pub started_at_ms: u64,
    pub duration_ms: u64,
    pub problems: Vec<ExamProblem>,
    pub submissions: Vec<Submission>,
    /// 按下「結束評量」的時間；時間到不會寫入，由 `is_over` 判斷。
    pub ended_at_ms: Option<u64>,
    /// 考卷名稱（預約考卷才有）。
    #[serde(default)]
    pub title: Option<String>,
}

impl Exam {
    pub fn ends_at_ms(&self) -> u64 {
        self.started_at_ms + self.duration_ms
    }

    pub fn is_over(&self, now: u64) -> bool {
        self.ended_at_ms.is_some() || now >= self.ends_at_ms()
    }

    pub fn is_solved(&self, problem_id: &str) -> bool {
        self.submissions.iter().any(|s| s.problem_id == problem_id && s.verdict == Verdict::Correct)
    }
}

/// 練習區每題的紀錄（不計分）。
#[derive(Debug, Clone, Serialize, Deserialize, Default)]
#[serde(rename_all = "camelCase")]
pub struct PracticeRecord {
    pub attempts: u32,
    /// 第一次通過正式評判的時間。
    pub solved_at_ms: Option<u64>,
    pub last_verdict: Option<Verdict>,
}

/// 預約的考卷（考古題整場重考、預測模擬卷）。下次登入時用它出題，而不是隨機抽題。
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct PlannedExam {
    /// 顯示用名稱，例如「2025/12/09 CPE 考古題」。
    pub title: String,
    pub problem_ids: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
#[serde(rename_all = "camelCase")]
pub struct Session {
    pub phase: Phase,
    pub examinee: Option<Examinee>,
    pub exam: Option<Exam>,
    #[serde(default)]
    pub practice: BTreeMap<String, PracticeRecord>,
    #[serde(default)]
    pub planned: Option<PlannedExam>,
}

/// 考試長度：3 小時。
pub const EXAM_DURATION_MS: u64 = 3 * 60 * 60 * 1000;

#[derive(Debug, PartialEq, Eq)]
pub enum SessionError {
    NotInExam,
    ExamOver,
    NotAnExamProblem,
}

impl std::fmt::Display for SessionError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str(match self {
            SessionError::NotInExam => "目前不在考試中",
            SessionError::ExamOver => "考試時間已結束",
            SessionError::NotAnExamProblem => "這一題不是本次考題",
        })
    }
}

impl Session {
    pub fn agree_license(&mut self) {
        if self.phase == Phase::License {
            self.phase = Phase::Login;
        }
    }

    /// 預約下一場考試的題目，並回到登入畫面（原本的考試會被清掉）。
    pub fn plan_exam(&mut self, planned: PlannedExam) {
        self.reset_exam();
        self.phase = Phase::Login;
        self.planned = Some(planned);
    }

    /// 登入並開始一場新的考試。有預約考卷時，用預約的題目並清除預約。
    pub fn login_and_start(&mut self, examinee: Examinee, problem_ids: &[String], now: u64) {
        let (problem_ids, title) = match self.planned.take() {
            Some(p) => (p.problem_ids, Some(p.title)),
            None => (problem_ids.to_vec(), None),
        };
        let code = "00A".to_string();
        let problems = problem_ids
            .iter()
            .enumerate()
            .map(|(i, id)| ExamProblem { label: format!("{code}{}", i + 1), problem_id: id.clone() })
            .collect();
        self.examinee = Some(examinee);
        self.exam = Some(Exam {
            code,
            started_at_ms: now,
            duration_ms: EXAM_DURATION_MS,
            problems,
            submissions: Vec::new(),
            ended_at_ms: None,
            title,
        });
        self.phase = Phase::Exam;
    }

    /// 記錄一次正式評判。已經答對的題目再交不會被記錄（避免多算罰時）。
    pub fn record_submission(&mut self, problem_id: &str, verdict: Verdict, now: u64) -> Result<(), SessionError> {
        let exam = self.exam.as_mut().ok_or(SessionError::NotInExam)?;
        if exam.is_over(now) {
            return Err(SessionError::ExamOver);
        }
        if !exam.problems.iter().any(|p| p.problem_id == problem_id) {
            return Err(SessionError::NotAnExamProblem);
        }
        if exam.is_solved(problem_id) {
            return Ok(());
        }
        let minute = (now.saturating_sub(exam.started_at_ms)) / 60_000;
        exam.submissions.push(Submission { problem_id: problem_id.to_string(), at_ms: now, minute, verdict });
        Ok(())
    }

    pub fn record_practice(&mut self, problem_id: &str, verdict: Verdict, now: u64) {
        let rec = self.practice.entry(problem_id.to_string()).or_default();
        rec.attempts += 1;
        rec.last_verdict = Some(verdict);
        if verdict == Verdict::Correct && rec.solved_at_ms.is_none() {
            rec.solved_at_ms = Some(now);
        }
    }

    pub fn end_exam(&mut self, now: u64) {
        if let Some(exam) = self.exam.as_mut() {
            if exam.ended_at_ms.is_none() {
                exam.ended_at_ms = Some(now.min(exam.ends_at_ms()));
            }
        }
    }

    /// 回到授權頁，清掉考試（練習紀錄保留）。
    pub fn reset_exam(&mut self) {
        self.phase = Phase::License;
        self.examinee = None;
        self.exam = None;
    }
}

/// 程式碼草稿與存檔。
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct CodeDraft {
    pub problem_id: String,
    pub lang: String,
    pub source: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct SavedCode {
    /// 顯示在「提檔續答」清單中的名稱。
    pub name: String,
    pub created_at_ms: u64,
    #[serde(flatten)]
    pub code: CodeDraft,
}

/// 把 Session、草稿、存檔放在 app data 目錄下。
pub struct Store {
    dir: PathBuf,
}

impl Store {
    pub fn new(dir: PathBuf) -> io::Result<Self> {
        std::fs::create_dir_all(dir.join("drafts"))?;
        std::fs::create_dir_all(dir.join("saves"))?;
        Ok(Store { dir })
    }

    fn session_path(&self) -> PathBuf {
        self.dir.join("session.json")
    }

    /// 讀取失敗（第一次啟動或檔案損毀）時回傳全新的 Session。
    pub fn load_session(&self) -> Session {
        std::fs::read(self.session_path())
            .ok()
            .and_then(|b| serde_json::from_slice(&b).ok())
            .unwrap_or_default()
    }

    pub fn save_session(&self, s: &Session) -> io::Result<()> {
        write_atomic(&self.session_path(), &serde_json::to_vec_pretty(s)?)
    }

    fn draft_path(&self, scope: &str, problem_id: &str) -> PathBuf {
        self.dir.join("drafts").join(format!("{}-{}.json", safe(scope), safe(problem_id)))
    }

    pub fn load_draft(&self, scope: &str, problem_id: &str) -> Option<CodeDraft> {
        let b = std::fs::read(self.draft_path(scope, problem_id)).ok()?;
        serde_json::from_slice(&b).ok()
    }

    pub fn save_draft(&self, scope: &str, draft: &CodeDraft) -> io::Result<()> {
        write_atomic(&self.draft_path(scope, &draft.problem_id), &serde_json::to_vec(draft)?)
    }

    pub fn clear_drafts(&self, scope: &str) -> io::Result<()> {
        let prefix = format!("{}-", safe(scope));
        for entry in std::fs::read_dir(self.dir.join("drafts"))? {
            let entry = entry?;
            if entry.file_name().to_string_lossy().starts_with(&prefix) {
                std::fs::remove_file(entry.path())?;
            }
        }
        Ok(())
    }

    /// 存一份程式碼（封卷存檔 / 另存新檔）。
    pub fn save_code(&self, name: &str, code: CodeDraft, now: u64) -> io::Result<SavedCode> {
        let saved = SavedCode { name: name.to_string(), created_at_ms: now, code };
        let file = format!("{now}-{}.json", safe(name));
        write_atomic(&self.dir.join("saves").join(file), &serde_json::to_vec(&saved)?)?;
        Ok(saved)
    }

    /// 所有存檔，新的在前。
    pub fn list_saves(&self) -> io::Result<Vec<SavedCode>> {
        let mut saves: Vec<SavedCode> = std::fs::read_dir(self.dir.join("saves"))?
            .filter_map(|e| e.ok())
            .filter_map(|e| std::fs::read(e.path()).ok())
            .filter_map(|b| serde_json::from_slice(&b).ok())
            .collect();
        saves.sort_by_key(|s| std::cmp::Reverse(s.created_at_ms));
        Ok(saves)
    }
}

/// 只留下可以當檔名的字元。
fn safe(s: &str) -> String {
    s.chars().map(|c| if c.is_alphanumeric() || c == '-' || c == '_' { c } else { '_' }).collect()
}

fn write_atomic(path: &Path, data: &[u8]) -> io::Result<()> {
    let tmp = path.with_extension("tmp");
    std::fs::write(&tmp, data)?;
    std::fs::rename(tmp, path)
}

#[cfg(test)]
mod tests {
    use super::*;

    fn examinee() -> Examinee {
        Examinee { id_no: "A123456789".into(), name: "模擬考生".into(), ticket: "SIM0001".into(), auth_code: "123456".into() }
    }

    fn started(now: u64) -> Session {
        let mut s = Session::default();
        s.agree_license();
        s.login_and_start(examinee(), &["272".into(), "10035".into()], now);
        s
    }

    #[test]
    fn phases_advance() {
        let mut s = Session::default();
        assert_eq!(s.phase, Phase::License);
        s.agree_license();
        assert_eq!(s.phase, Phase::Login);
        s.login_and_start(examinee(), &["272".into()], 0);
        assert_eq!(s.phase, Phase::Exam);
        assert_eq!(s.exam.as_ref().unwrap().problems[0].label, "00A1");
    }

    #[test]
    fn submissions_record_minutes_from_start() {
        let mut s = started(1_000);
        s.record_submission("272", Verdict::WrongAnswer, 1_000 + 15 * 60_000 + 59_999).unwrap();
        s.record_submission("272", Verdict::Correct, 1_000 + 32 * 60_000).unwrap();
        let minutes: Vec<_> = s.exam.as_ref().unwrap().submissions.iter().map(|x| x.minute).collect();
        assert_eq!(minutes, [15, 32]);
    }

    #[test]
    fn submissions_after_correct_are_ignored() {
        let mut s = started(0);
        s.record_submission("272", Verdict::Correct, 60_000).unwrap();
        s.record_submission("272", Verdict::WrongAnswer, 120_000).unwrap();
        assert_eq!(s.exam.as_ref().unwrap().submissions.len(), 1);
    }

    #[test]
    fn submissions_rejected_when_over_or_foreign() {
        let mut s = started(0);
        assert_eq!(s.record_submission("100", Verdict::Correct, 1), Err(SessionError::NotAnExamProblem));
        assert_eq!(s.record_submission("272", Verdict::Correct, EXAM_DURATION_MS), Err(SessionError::ExamOver));
        let mut s = started(0);
        s.end_exam(10);
        assert_eq!(s.record_submission("272", Verdict::Correct, 20), Err(SessionError::ExamOver));
        assert_eq!(Session::default().record_submission("272", Verdict::Correct, 0), Err(SessionError::NotInExam));
    }

    #[test]
    fn planned_exam_overrides_draw_once() {
        let mut s = started(0);
        s.plan_exam(PlannedExam { title: "2025/12/09 CPE".into(), problem_ids: vec!["10079".into(), "11321".into()] });
        assert_eq!(s.phase, Phase::Login);
        assert!(s.exam.is_none());
        s.login_and_start(examinee(), &["272".into()], 5);
        let exam = s.exam.as_ref().unwrap();
        let ids: Vec<_> = exam.problems.iter().map(|p| p.problem_id.as_str()).collect();
        assert_eq!(ids, ["10079", "11321"]);
        assert_eq!(exam.title.as_deref(), Some("2025/12/09 CPE"));
        assert!(s.planned.is_none());
        // 下一場又回到隨機抽題
        s.login_and_start(examinee(), &["272".into()], 6);
        assert_eq!(s.exam.as_ref().unwrap().problems[0].problem_id, "272");
    }

    #[test]
    fn practice_records_first_solve() {
        let mut s = Session::default();
        s.record_practice("272", Verdict::WrongAnswer, 5);
        s.record_practice("272", Verdict::Correct, 9);
        s.record_practice("272", Verdict::Correct, 12);
        let r = &s.practice["272"];
        assert_eq!((r.attempts, r.solved_at_ms), (3, Some(9)));
    }

    #[test]
    fn store_round_trips() {
        let dir = tempfile::tempdir().unwrap();
        let store = Store::new(dir.path().to_path_buf()).unwrap();
        assert_eq!(store.load_session().phase, Phase::License);
        let s = started(42);
        store.save_session(&s).unwrap();
        assert_eq!(store.load_session().exam.unwrap().started_at_ms, 42);

        let draft = CodeDraft { problem_id: "272".into(), lang: "ccpp".into(), source: "int main(){}".into() };
        store.save_draft("exam", &draft).unwrap();
        assert_eq!(store.load_draft("exam", "272"), Some(draft.clone()));
        assert_eq!(store.load_draft("practice", "272"), None);
        store.clear_drafts("exam").unwrap();
        assert_eq!(store.load_draft("exam", "272"), None);

        store.save_code("CPE_TEST", draft.clone(), 1).unwrap();
        store.save_code("(14-59-26)auto", draft, 2).unwrap();
        let names: Vec<_> = store.list_saves().unwrap().into_iter().map(|s| s.name).collect();
        assert_eq!(names, ["(14-59-26)auto", "CPE_TEST"]);
    }
}
