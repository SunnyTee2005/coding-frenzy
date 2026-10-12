#include <iostream>
#include <map>
#include <sstream>
#include <string>
using namespace std;
int main() {
    string line;
    getline(cin, line);
    int n = stoi(line);
    map<string, int> cnt;
    for (int i = 0; i < n && getline(cin, line); ++i) {
        istringstream in(line);
        string country;
        in >> country;
        ++cnt[country];
    }
    for (auto& p : cnt) cout << p.first << " " << p.second << "\n";
}
