#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
int main() {
    int t; cin >> t;
    for (int c = 0; c < t; ++c) {
        int n, h; cin >> n >> h;
        string s = string(n - h, '0') + string(h, '1');
        if (c) cout << "\n";
        do cout << s << "\n"; while (next_permutation(s.begin(), s.end()));
    }
}
