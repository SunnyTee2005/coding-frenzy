#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main() {
    string line;
    while (getline(cin, line)) {
        istringstream in(line);
        long long x = 1, p, e;
        bool any = false;
        while (in >> p) {
            if (p == 0 && !any) return 0;
            in >> e; any = true;
            while (e--) x *= p;
        }
        if (!any) continue;
        --x;
        vector<pair<long long, int>> f;
        for (long long q = 2; q * q <= x; ++q)
            if (x % q == 0) { int c = 0; while (x % q == 0) { x /= q; ++c; } f.push_back({q, c}); }
        if (x > 1) f.push_back({x, 1});
        for (int i = (int)f.size() - 1; i >= 0; --i)
            cout << f[i].first << " " << f[i].second << (i ? " " : "\n");
    }
}
