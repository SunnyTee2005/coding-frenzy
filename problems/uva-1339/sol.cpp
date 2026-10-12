#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
int main() {
    string a, b;
    while (cin >> a >> b) {
        int ca[26] = {}, cb[26] = {};
        for (char c : a) ++ca[c - 'A'];
        for (char c : b) ++cb[c - 'A'];
        sort(ca, ca + 26);
        sort(cb, cb + 26);
        cout << (equal(ca, ca + 26, cb) ? "YES" : "NO") << "\n";
    }
}
