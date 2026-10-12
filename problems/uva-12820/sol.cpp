#include <iostream>
#include <set>
#include <string>
using namespace std;
int main() {
    int n, c = 0;
    while (cin >> n) {
        int cool = 0;
        while (n--) {
            string w; cin >> w;
            int f[26] = {};
            for (char ch : w) ++f[ch - 'a'];
            set<int> seen;
            int distinct = 0;
            bool ok = true;
            for (int x : f) if (x) { ++distinct; if (!seen.insert(x).second) ok = false; }
            if (ok && distinct >= 2) ++cool;
        }
        cout << "Case " << ++c << ": " << cool << "\n";
    }
}
