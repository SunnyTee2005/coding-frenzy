#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    string line;
    bool first = true;
    while (getline(cin, line)) {
        int cnt[128] = {};
        for (char c : line) if (c != '\r' && c != '\n') ++cnt[(unsigned char)c & 127];
        vector<pair<int, int>> v;  // (次數, -ASCII)
        for (int i = 0; i < 128; ++i) if (cnt[i]) v.push_back({cnt[i], -i});
        sort(v.begin(), v.end());
        if (!first) cout << "\n";
        first = false;
        for (auto& p : v) cout << -p.second << " " << p.first << "\n";
    }
}
