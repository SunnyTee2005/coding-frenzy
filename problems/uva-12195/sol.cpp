#include <iostream>
#include <string>
using namespace std;
int main() {
    string s;
    while (cin >> s && s != "*") {
        int cnt = 0, sum = 0;  // 以 1/64 為單位
        for (size_t i = 1; i < s.size(); ++i) {
            char c = s[i];
            if (c == '/') { if (sum == 64) ++cnt; sum = 0; continue; }
            switch (c) {
                case 'W': sum += 64; break;
                case 'H': sum += 32; break;
                case 'Q': sum += 16; break;
                case 'E': sum += 8; break;
                case 'S': sum += 4; break;
                case 'T': sum += 2; break;
                case 'X': sum += 1; break;
            }
        }
        cout << cnt << "\n";
    }
}
