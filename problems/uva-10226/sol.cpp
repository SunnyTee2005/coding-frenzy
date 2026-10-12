#include <cstdio>
#include <iostream>
#include <map>
#include <string>
using namespace std;
int main() {
    string line;
    getline(cin, line);
    int t = stoi(line);
    getline(cin, line);
    for (int c = 0; c < t; ++c) {
        map<string, int> cnt;
        int total = 0;
        while (getline(cin, line)) {
            if (!line.empty() && line.back() == '\r') line.pop_back();
            if (line.empty()) break;
            ++cnt[line]; ++total;
        }
        if (c) printf("\n");
        for (auto &p : cnt) printf("%s %.4f\n", p.first.c_str(), 100.0 * p.second / total);
    }
}
