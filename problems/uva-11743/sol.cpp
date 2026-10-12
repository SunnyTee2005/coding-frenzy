#include <iostream>
#include <string>
using namespace std;
int main() {
    int n; cin >> n;
    while (n--) {
        string d, g;
        for (int i = 0; i < 4; ++i) { cin >> g; d += g; }
        int sum = 0;
        for (int i = 0; i < 16; ++i) {
            int v = d[i] - '0';
            if (i % 2 == 0) { v *= 2; sum += v / 10 + v % 10; }
            else sum += v;
        }
        cout << (sum % 10 == 0 ? "Valid" : "Invalid") << "\n";
    }
}
