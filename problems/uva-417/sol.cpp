#include <iostream>
#include <map>
#include <string>
using namespace std;
map<string, int> idx;
int counter = 0;
void gen(string cur, char from, int len) {
    if ((int)cur.size() == len) { idx[cur] = ++counter; return; }
    for (char c = from; c <= 'z'; ++c) gen(cur + c, c + 1, len);
}
int main() {
    for (int len = 1; len <= 5; ++len) gen("", 'a', len);
    string w;
    while (cin >> w) {
        auto it = idx.find(w);
        cout << (it == idx.end() ? 0 : it->second) << "\n";
    }
}
