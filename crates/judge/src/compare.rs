use crate::Verdict;

/// 比對預期輸出與實際輸出。
///
/// - 換行統一成 `\n`（Windows 程式會輸出 `\r\n`），檔尾多或少的換行不計較。
/// - 完全相同 → CORRECT。
/// - 只差在空白 / 換行的位置或數量 → PRESENTATION-ERROR。
/// - 預期有輸出、實際完全沒有 → NO-OUTPUT。
/// - 其餘 → WRONG-ANSWER。
///
/// TODO(Phase 0)：對照原程式的比對規則（尤其行尾空白、檔尾換行）調整。
pub fn compare(expected: &[u8], actual: &[u8]) -> Verdict {
    let expected = normalize_newlines(expected);
    let actual = normalize_newlines(actual);
    if is_blank(&actual) && !is_blank(&expected) {
        return Verdict::NoOutput;
    }
    if trim_trailing_newlines(&expected) == trim_trailing_newlines(&actual) {
        return Verdict::Correct;
    }
    if tokens(&expected).eq(tokens(&actual)) {
        return Verdict::PresentationError;
    }
    Verdict::WrongAnswer
}

fn normalize_newlines(s: &[u8]) -> Vec<u8> {
    let mut out = Vec::with_capacity(s.len());
    let mut i = 0;
    while i < s.len() {
        if s[i] == b'\r' && s.get(i + 1) == Some(&b'\n') {
            i += 1;
            continue;
        }
        out.push(s[i]);
        i += 1;
    }
    out
}

fn trim_trailing_newlines(s: &[u8]) -> &[u8] {
    let end = s.iter().rposition(|&b| b != b'\n').map_or(0, |p| p + 1);
    &s[..end]
}

fn is_blank(s: &[u8]) -> bool {
    s.iter().all(u8::is_ascii_whitespace)
}

fn tokens(s: &[u8]) -> impl Iterator<Item = &[u8]> {
    s.split(u8::is_ascii_whitespace).filter(|t| !t.is_empty())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn exact_match_is_correct() {
        assert_eq!(compare(b"1 2\n3\n", b"1 2\n3\n"), Verdict::Correct);
    }

    #[test]
    fn crlf_and_final_newline_are_tolerated() {
        assert_eq!(compare(b"1 2\n3\n", b"1 2\r\n3\r\n"), Verdict::Correct);
        assert_eq!(compare(b"1 2\n3\n", b"1 2\n3"), Verdict::Correct);
        assert_eq!(compare(b"1 2\n3", b"1 2\n3\n\n"), Verdict::Correct);
    }

    #[test]
    fn whitespace_difference_is_presentation_error() {
        assert_eq!(compare(b"1 2\n3\n", b"1  2\n3\n"), Verdict::PresentationError);
        assert_eq!(compare(b"1 2\n3\n", b"1 2 3\n"), Verdict::PresentationError);
        assert_eq!(compare(b"1 2\n3\n", b"1 2 \n3\n"), Verdict::PresentationError);
    }

    #[test]
    fn empty_output_is_no_output() {
        assert_eq!(compare(b"1\n", b""), Verdict::NoOutput);
        assert_eq!(compare(b"1\n", b"\n \n"), Verdict::NoOutput);
        assert_eq!(compare(b"", b""), Verdict::Correct);
    }

    #[test]
    fn different_content_is_wrong_answer() {
        assert_eq!(compare(b"1 2\n3\n", b"1 2\n4\n"), Verdict::WrongAnswer);
        assert_eq!(compare(b"1 2\n3\n", b"1 2\n"), Verdict::WrongAnswer);
    }
}
