use serde::{Deserialize, Serialize};

/// 一種程式語言的編譯 / 執行設定，來源是 `languages.toml`。
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Language {
    pub id: String,
    pub display: String,
    pub source: String,
    pub programs: Vec<String>,
    #[serde(default)]
    pub compile: Option<Vec<String>>,
    pub run: Vec<String>,
}

#[derive(Deserialize)]
struct LanguageFile {
    language: Vec<Language>,
}

/// 內建的語言清單（CCPP:MinGW、Python）。
pub fn builtin_languages() -> Vec<Language> {
    let file: LanguageFile =
        toml::from_str(include_str!("../languages.toml")).expect("languages.toml 格式錯誤");
    file.language
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn builtin_table_parses() {
        let ids: Vec<_> = builtin_languages().into_iter().map(|l| l.id).collect();
        assert_eq!(ids, ["ccpp", "python"]);
    }
}
