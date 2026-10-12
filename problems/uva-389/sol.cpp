#include <iostream>
#include <string>
using namespace std;
int main() {
    const string D = "0123456789ABCDEF";
    string s;
    int from, to;
    while (cin >> s >> from >> to) {
        long long v = 0;
        for (char c : s) v = v * from + (long long)D.find(c);
        string r;
        do { r = D[v % to] + r; v /= to; } while (v);
        if (r.size() > 7) r = r.substr(r.size() - 7);
        cout << string(7 - r.size(), '0') << r << "\n";
    }
}
