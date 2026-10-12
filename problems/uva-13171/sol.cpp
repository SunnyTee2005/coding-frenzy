#include <iostream>
#include <string>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        long long m, y, c; string s;
        cin >> m >> y >> c >> s;
        for (char p : s) {
            if (p == 'M' || p == 'R' || p == 'B' || p == 'V') --m;
            if (p == 'Y' || p == 'R' || p == 'B' || p == 'G') --y;
            if (p == 'C' || p == 'B' || p == 'G' || p == 'V') --c;
        }
        if (m < 0 || y < 0 || c < 0) cout << "NO\n";
        else cout << "YES " << m << " " << y << " " << c << "\n";
    }
}
