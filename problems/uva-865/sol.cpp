#include <iostream>
#include <string>
using namespace std;
int main() {
    string line;
    getline(cin, line);
    int t = stoi(line);
    getline(cin, line);  // 空白行
    for (int c = 0; c < t; ++c) {
        string plain, sub;
        getline(cin, plain);
        getline(cin, sub);
        if (c) cout << "\n";
        cout << sub << "\n" << plain << "\n";
        char m[256];
        for (int i = 0; i < 256; ++i) m[i] = (char)i;
        for (size_t i = 0; i < plain.size() && i < sub.size(); ++i) m[(unsigned char)plain[i]] = sub[i];
        while (getline(cin, line) && !line.empty()) {
            for (char& ch : line) ch = m[(unsigned char)ch];
            cout << line << "\n";
        }
    }
}
