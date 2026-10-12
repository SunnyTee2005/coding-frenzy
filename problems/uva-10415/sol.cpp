#include <cstring>
#include <iostream>
#include <string>
using namespace std;
int main() {
    const string notes = "cdefgabCDEFGAB";
    const char* fingers[] = {"0111001111", "0111001110", "0111001100", "0111001000", "0111000000", "0110000000", "0100000000",
                             "0010000000", "1111001110", "1111001100", "1111001000", "1111000000", "1110000000", "1100000000"};
    string line;
    getline(cin, line);
    int t = stoi(line);
    while (t--) {
        if (!getline(cin, line)) line = "";
        int cnt[10] = {};
        const char* prev = "0000000000";
        for (char c : line) {
            size_t k = notes.find(c);
            if (k == string::npos) continue;
            const char* cur = fingers[k];
            for (int i = 0; i < 10; ++i) if (cur[i] == '1' && prev[i] == '0') ++cnt[i];
            prev = cur;
        }
        for (int i = 0; i < 10; ++i) cout << cnt[i] << (i < 9 ? " " : "\n");
    }
}
