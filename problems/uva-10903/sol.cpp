#include <cstdio>
#include <cstring>
int code(const char* s) { return s[0] == 'r' ? 0 : s[0] == 'p' ? 1 : 2; }
int main() {
    int n, k;
    bool first = true;
    while (scanf("%d", &n) == 1 && n) {
        scanf("%d", &k);
        int w[105] = {}, l[105] = {};
        int games = k * n * (n - 1) / 2;
        for (int i = 0; i < games; ++i) {
            int p1, p2; char m1[16], m2[16];
            scanf("%d %s %d %s", &p1, m1, &p2, m2);
            int a = code(m1), b = code(m2);
            if (a == b) continue;
            // rock(0) < paper(1) < scissors(2) < rock：b 剛好是 a 的下一個時 b 贏
            if ((a + 1) % 3 == b) { ++w[p2]; ++l[p1]; } else { ++w[p1]; ++l[p2]; }
        }
        if (!first) printf("\n");
        first = false;
        for (int i = 1; i <= n; ++i) {
            if (w[i] + l[i] == 0) puts("-");
            else printf("%.3f\n", (double)w[i] / (w[i] + l[i]));
        }
    }
}
