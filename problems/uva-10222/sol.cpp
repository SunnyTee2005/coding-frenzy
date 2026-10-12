#include <cctype>
#include <iostream>
#include <string>
using namespace std;
int main() {
    const string kb = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./";
    string line;
    getline(cin, line);
    int n = stoi(line);
    while (n-- && getline(cin, line)) {
        for (char& c : line) {
            size_t p = kb.find((char)tolower((unsigned char)c));
            if (c != ' ' && p != string::npos && p >= 2) c = kb[p - 2];
        }
        cout << line << "\n";
    }
}
