#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    int t; cin >> t;
    for (int c = 0; c < t; ++c) {
        int d; cin >> d;
        vector<string> name(d);
        vector<int> lo(d), hi(d);
        for (int i = 0; i < d; ++i) cin >> name[i] >> lo[i] >> hi[i];
        int q; cin >> q;
        if (c) cout << "\n";
        while (q--) {
            int p; cin >> p;
            int found = -1, cnt = 0;
            for (int i = 0; i < d; ++i) if (lo[i] <= p && p <= hi[i]) { ++cnt; found = i; }
            cout << (cnt == 1 ? name[found] : "UNDETERMINED") << "\n";
        }
    }
}
