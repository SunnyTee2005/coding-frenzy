#include <iostream>
#include <string>
using namespace std;
int main() {
    const string keys = "22233344455566677778889999";
    string s;
    while (getline(cin, s)) {
        if (!s.empty() && s.back() == '\r') s.pop_back();
        if (s.empty()) continue;
        int letters = 0, hyphens = 0;
        for (char &c : s) {
            if (c >= 'A' && c <= 'Z') { c = keys[c - 'A']; ++letters; }
            else if (c == '-') ++hyphens;
        }
        cout << s << " " << letters << " " << hyphens << "\n";
    }
}
