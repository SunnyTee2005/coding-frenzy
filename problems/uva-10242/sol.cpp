#include <cstdio>
int main() {
    double x[4], y[4];
    while (scanf("%lf %lf %lf %lf %lf %lf %lf %lf", &x[0], &y[0], &x[1], &y[1], &x[2], &y[2], &x[3], &y[3]) == 8) {
        // 找出兩邊共用的端點 (i, j)，第四點 = 另外兩端點相加 - 共用點
        int si = 0, sj = 2;
        for (int i = 0; i < 2; ++i)
            for (int j = 2; j < 4; ++j)
                if (x[i] == x[j] && y[i] == y[j]) { si = i; sj = j; }
        int oi = 1 - si, oj = 5 - sj;
        printf("%.3f %.3f\n", x[oi] + x[oj] - x[si], y[oi] + y[oj] - y[si]);
    }
}
