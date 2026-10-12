#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
int main() {
    int t; cin >> t;
    long long fact[21] = {1};
    for (int i = 1; i <= 20; ++i) fact[i] = fact[i - 1] * i;
    while (t--) {
        string s; long long n;
        cin >> s >> n;
        sort(s.begin(), s.end());
        string out;
        while (!s.empty()) {
            long long f = fact[s.size() - 1];
            int i = (int)(n / f);
            out += s[i];
            s.erase(s.begin() + i);
            n %= f;
        }
        cout << out << "\n";
    }
}
