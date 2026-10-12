#include <cctype>
#include <iostream>
#include <string>
using namespace std;
int main() {
    string line;
    while (getline(cin, line)) {
        int cnt[128] = {};
        for (char c : line) if (isalpha((unsigned char)c)) ++cnt[(unsigned char)c];
        int best = 0;
        for (int i = 0; i < 128; ++i) if (cnt[i] > best) best = cnt[i];
        string s;
        for (int i = 'A'; i <= 'Z'; ++i) if (cnt[i] == best) s += char(i);
        for (int i = 'a'; i <= 'z'; ++i) if (cnt[i] == best) s += char(i);
        cout << s << " " << best << "\n";
    }
}
