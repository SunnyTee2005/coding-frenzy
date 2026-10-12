#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>
using namespace std;
int main() {
    vector<string> words;
    map<string, int> id;
    string line;
    while (getline(cin, line) && !line.empty()) {
        if (!id.count(line)) { id[line] = (int)words.size(); words.push_back(line); }
    }
    // 依「挖掉一個字母」的樣式分組，同組的字互為 doublet
    map<string, vector<int>> bucket;
    for (int i = 0; i < (int)words.size(); ++i)
        for (size_t p = 0; p < words[i].size(); ++p) {
            string key = words[i]; key[p] = '*';
            bucket[key].push_back(i);
        }
    bool first = true;
    string a, b;
    while (cin >> a >> b) {
        if (!first) cout << "\n";
        first = false;
        if (!id.count(a) || !id.count(b) || a.size() != b.size()) { cout << "No solution.\n"; continue; }
        int s = id[a], t = id[b];
        vector<int> prev(words.size(), -2);
        queue<int> q; q.push(s); prev[s] = -1;
        while (!q.empty() && prev[t] == -2) {
            int u = q.front(); q.pop();
            for (size_t p = 0; p < words[u].size(); ++p) {
                string key = words[u]; key[p] = '*';
                for (int v : bucket[key]) if (prev[v] == -2) { prev[v] = u; q.push(v); }
            }
        }
        if (prev[t] == -2) { cout << "No solution.\n"; continue; }
        vector<int> path;
        for (int v = t; v != -1; v = prev[v]) path.push_back(v);
        for (int i = (int)path.size() - 1; i >= 0; --i) cout << words[path[i]] << "\n";
    }
}
