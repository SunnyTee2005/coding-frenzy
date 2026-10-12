//! 題文：和考場一樣直接顯示 UVa 原文 PDF。
//!
//! PDF 不打包進 App，第一次開題時才從公開網址下載（先 onlinejudge.org、再 CPE 鏡像），
//! 存在 app data 的 `statements/` 快取，之後離線也能看。

use std::io;
use std::path::{Path, PathBuf};
use std::time::Duration;

/// 依序嘗試的下載來源。
pub fn default_sources(uva: u32) -> Vec<String> {
    vec![
        format!("https://onlinejudge.org/external/{}/{uva}.pdf", uva / 100),
        format!("https://cpe.mcu.edu.tw/cpe/problemPdf/{uva}.pdf"),
    ]
}

pub struct StatementCache {
    dir: PathBuf,
}

impl StatementCache {
    pub fn new(dir: PathBuf) -> io::Result<Self> {
        std::fs::create_dir_all(&dir)?;
        Ok(StatementCache { dir })
    }

    fn path(&self, uva: u32) -> PathBuf {
        self.dir.join(format!("{uva}.pdf"))
    }

    /// 取得 PDF：有快取就用快取，否則依序下載 `sources`，第一個成功的寫入快取。
    pub fn get(&self, uva: u32, sources: &[String]) -> Result<Vec<u8>, String> {
        if let Ok(bytes) = std::fs::read(self.path(uva)) {
            if is_pdf(&bytes) {
                return Ok(bytes);
            }
        }
        let client = reqwest::blocking::Client::builder()
            .timeout(Duration::from_secs(20))
            .user_agent("cpe-sim (CPE practice simulator)")
            .build()
            .map_err(|e| e.to_string())?;
        let mut errors = Vec::new();
        for url in sources {
            match download(&client, url) {
                Ok(bytes) => {
                    write_atomic(&self.path(uva), &bytes).map_err(|e| e.to_string())?;
                    return Ok(bytes);
                }
                Err(e) => errors.push(format!("{url}：{e}")),
            }
        }
        Err(format!("無法下載題目 PDF（UVa {uva}），請確認網路連線。\n{}", errors.join("\n")))
    }
}

fn download(client: &reqwest::blocking::Client, url: &str) -> Result<Vec<u8>, String> {
    let resp = client.get(url).send().map_err(|e| e.to_string())?;
    if !resp.status().is_success() {
        return Err(format!("HTTP {}", resp.status().as_u16()));
    }
    let bytes = resp.bytes().map_err(|e| e.to_string())?.to_vec();
    // 有些網站找不到檔案時仍回 200 加 HTML 頁面
    if !is_pdf(&bytes) {
        return Err("回應不是 PDF".into());
    }
    Ok(bytes)
}

fn is_pdf(bytes: &[u8]) -> bool {
    bytes.starts_with(b"%PDF")
}

fn write_atomic(path: &Path, data: &[u8]) -> io::Result<()> {
    let tmp = path.with_extension("tmp");
    std::fs::write(&tmp, data)?;
    std::fs::rename(tmp, path)
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::io::{Read, Write};
    use std::net::TcpListener;

    /// 啟動一個簡單的本機 HTTP 伺服器：路徑對應到 (狀態碼, 內容)。回傳基底網址。
    fn serve(routes: Vec<(&'static str, u16, &'static [u8])>) -> String {
        let listener = TcpListener::bind("127.0.0.1:0").unwrap();
        let addr = listener.local_addr().unwrap();
        std::thread::spawn(move || {
            for stream in listener.incoming() {
                let mut s = stream.unwrap();
                let mut buf = [0u8; 2048];
                let n = s.read(&mut buf).unwrap_or(0);
                let req = String::from_utf8_lossy(&buf[..n]);
                let path = req.split_whitespace().nth(1).unwrap_or("/").to_string();
                let (code, body) = routes
                    .iter()
                    .find(|(p, _, _)| *p == path)
                    .map(|(_, c, b)| (*c, *b))
                    .unwrap_or((404, b"not found" as &[u8]));
                let head = format!("HTTP/1.1 {code} X\r\nContent-Length: {}\r\nConnection: close\r\n\r\n", body.len());
                let _ = s.write_all(head.as_bytes());
                let _ = s.write_all(body);
            }
        });
        format!("http://{addr}")
    }

    #[test]
    fn falls_back_to_second_source_and_caches() {
        let base = serve(vec![("/a.pdf", 404, b"nope"), ("/b.pdf", 200, b"%PDF-1.4 fake")]);
        let dir = tempfile::tempdir().unwrap();
        let cache = StatementCache::new(dir.path().to_path_buf()).unwrap();
        let sources = vec![format!("{base}/a.pdf"), format!("{base}/b.pdf")];
        assert_eq!(cache.get(100, &sources).unwrap(), b"%PDF-1.4 fake");
        // 第二次不需要網路：來源全部失效也拿得到
        assert_eq!(cache.get(100, &["http://127.0.0.1:1/x.pdf".into()]).unwrap(), b"%PDF-1.4 fake");
    }

    #[test]
    fn rejects_html_served_as_200() {
        let base = serve(vec![("/a.pdf", 200, b"<html>404 Page Not Found</html>")]);
        let dir = tempfile::tempdir().unwrap();
        let cache = StatementCache::new(dir.path().to_path_buf()).unwrap();
        let err = cache.get(101, &[format!("{base}/a.pdf")]).unwrap_err();
        assert!(err.contains("不是 PDF"), "{err}");
        assert!(!dir.path().join("101.pdf").exists());
    }

    #[test]
    fn reports_all_failures() {
        let base = serve(vec![]);
        let dir = tempfile::tempdir().unwrap();
        let cache = StatementCache::new(dir.path().to_path_buf()).unwrap();
        let err = cache.get(102, &[format!("{base}/a.pdf"), format!("{base}/b.pdf")]).unwrap_err();
        assert!(err.contains("HTTP 404"), "{err}");
        assert_eq!(err.matches("HTTP 404").count(), 2);
    }

    #[test]
    fn default_sources_use_uva_volume() {
        assert_eq!(default_sources(10189)[0], "https://onlinejudge.org/external/101/10189.pdf");
        assert_eq!(default_sources(272)[0], "https://onlinejudge.org/external/2/272.pdf");
    }
}
