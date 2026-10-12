#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    int n;
    string line;
    getline(cin, line);
    n = stoi(line);
    int cnt[26] = {};
    for (int i = 0; i < n && getline(cin, line); ++i)
        for (char c : line) if (isalpha((unsigned char)c)) ++cnt[toupper((unsigned char)c) - 'A'];
    vector<int> idx;
    for (int i = 0; i < 26; ++i) if (cnt[i]) idx.push_back(i);
    stable_sort(idx.begin(), idx.end(), [&](int a, int b) { return cnt[a] > cnt[b]; });
    for (int i : idx) cout << char('A' + i) << " " << cnt[i] << "\n";
}
