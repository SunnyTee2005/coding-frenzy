#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main() {
    string line;
    getline(cin, line);
    int t = stoi(line);
    getline(cin, line);  // 空行
    for (int c = 0; c < t; ++c) {
        bool seen[101] = {}, solved[101][10] = {};
        int wrong[101][10] = {}, cnt[101] = {}, pen[101] = {};
        while (getline(cin, line) && !line.empty() && line != "\r") {
            istringstream in(line);
            int who, prob, time; char L;
            if (!(in >> who >> prob >> time >> L)) continue;
            seen[who] = true;
            if (solved[who][prob]) continue;
            if (L == 'C') { solved[who][prob] = true; ++cnt[who]; pen[who] += time + 20 * wrong[who][prob]; }
            else if (L == 'I') ++wrong[who][prob];
        }
        vector<int> ids;
        for (int i = 1; i <= 100; ++i) if (seen[i]) ids.push_back(i);
        sort(ids.begin(), ids.end(), [&](int a, int b) {
            if (cnt[a] != cnt[b]) return cnt[a] > cnt[b];
            if (pen[a] != pen[b]) return pen[a] < pen[b];
            return a < b;
        });
        if (c) cout << "\n";
        for (int i : ids) cout << i << " " << cnt[i] << " " << pen[i] << "\n";
    }
}
