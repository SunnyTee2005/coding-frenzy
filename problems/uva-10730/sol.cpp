#include <cstdio>
#include <vector>
int main() {
    int n;
    while (scanf("%d:", &n) == 1 && n) {
        std::vector<int> p(n), pos(n);
        for (int i = 0; i < n; ++i) { scanf("%d", &p[i]); pos[p[i]] = i; }
        bool anti = true;
        for (int i = 0; i < n && anti; ++i)
            for (int j = i + 1; j < n && anti; ++j) {
                int c = 2 * p[j] - p[i];  // 等差數列的第三項
                if (c >= 0 && c < n && pos[c] > j) anti = false;
            }
        puts(anti ? "yes" : "no");
    }
}
