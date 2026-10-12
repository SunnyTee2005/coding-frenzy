#include <iostream>
#include <string>
using namespace std;
int main() {
    int t; cin >> t;
    for (int cs = 1; cs <= t; ++cs) {
        string url[10]; int v[10], best = 0;
        for (int i = 0; i < 10; ++i) { cin >> url[i] >> v[i]; if (v[i] > best) best = v[i]; }
        cout << "Case #" << cs << ":\n";
        for (int i = 0; i < 10; ++i) if (v[i] == best) cout << url[i] << "\n";
    }
}
