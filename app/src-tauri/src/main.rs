// release 版在 Windows 上不要多開一個主控台視窗
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
    cpe_sim_lib::run()
}
