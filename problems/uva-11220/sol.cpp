#include <iostream>
#include <sstream>
#include <string>
using namespace std;
int main() {
    string line;
    getline(cin, line);
    int t = stoi(line);
    getline(cin, line);  // 第一個案例前的空白行
    for (int c = 1; c <= t; ++c) {
        if (c > 1) cout << "\n";
        cout << "Case #" << c << ":\n";
        while (getline(cin, line) && line.find_first_not_of(" \t\r") != string::npos) {
            istringstream in(line);
            string w, dec;
            while (in >> w) if (w.size() > dec.size()) dec += w[dec.size()];
            cout << dec << "\n";
        }
    }
}
