#include <cctype>
#include <iostream>
#include <string>
using namespace std;
int main() {
    int t; cin >> t;
    for (int c = 1; c <= t; ++c) {
        string s, out; cin >> s;
        for (size_t i = 0; i < s.size();) {
            char ch = s[i++];
            int n = 0;
            while (i < s.size() && isdigit((unsigned char)s[i])) n = n * 10 + (s[i++] - '0');
            out.append(n, ch);
        }
        cout << "Case " << c << ": " << out << "\n";
    }
}
