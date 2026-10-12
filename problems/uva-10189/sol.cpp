#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int n, m, field = 0;
    while (cin >> n >> m && (n || m)) {
        vector<string> g(n);
        for (auto &row : g) cin >> row;
        if (field) cout << "\n";
        cout << "Field #" << ++field << ":\n";
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (g[i][j] == '*') { cout << '*'; continue; }
                int c = 0;
                for (int di = -1; di <= 1; ++di)
                    for (int dj = -1; dj <= 1; ++dj) {
                        int a = i + di, b = j + dj;
                        if (a >= 0 && a < n && b >= 0 && b < m && g[a][b] == '*') ++c;
                    }
                cout << c;
            }
            cout << "\n";
        }
    }
    return 0;
}
