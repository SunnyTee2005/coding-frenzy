#include <iostream>
#include <map>
#include <string>
using namespace std;
int main() {
    string line;
    getline(cin, line);
    int n = stoi(line);
    map<string, string> m;
    for (int i = 0; i < n; ++i) {
        string a, b;
        getline(cin, a); getline(cin, b);
        m[a] = b;
    }
    getline(cin, line);
    int q = stoi(line);
    while (q-- && getline(cin, line)) cout << m[line] << "\n";
}
