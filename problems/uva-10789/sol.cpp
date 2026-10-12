#include <iostream>
#include <string>
using namespace std;
bool prime(int n) {
    if (n < 2) return false;
    for (int d = 2; d * d <= n; ++d) if (n % d == 0) return false;
    return true;
}
int main() {
    int t; cin >> t;
    for (int c = 1; c <= t; ++c) {
        string s; cin >> s;
        int cnt[128] = {};
        for (char ch : s) ++cnt[(unsigned char)ch];
        string out;
        for (int i = 0; i < 128; ++i) if (prime(cnt[i])) out += char(i);
        cout << "Case " << c << ": " << (out.empty() ? "empty" : out) << "\n";
    }
}
