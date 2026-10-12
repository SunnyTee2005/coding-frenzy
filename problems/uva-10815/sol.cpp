#include <cctype>
#include <iostream>
#include <set>
#include <string>
using namespace std;
int main() {
    set<string> words;
    string cur;
    char c;
    while (cin.get(c)) {
        if (isalpha((unsigned char)c)) cur += (char)tolower((unsigned char)c);
        else if (!cur.empty()) { words.insert(cur); cur.clear(); }
    }
    if (!cur.empty()) words.insert(cur);
    for (const string& w : words) cout << w << "\n";
}
