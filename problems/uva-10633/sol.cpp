#include <cstdio>
int main() {
    unsigned long long x;
    while (scanf("%llu", &x) == 1 && x) {
        // N = 10M + d，N - M = 9M + d；d 從 9 往 0 試，得到的 N 由小到大
        bool first = true;
        for (int d = 9; d >= 0; --d) {
            if (x < (unsigned long long)d || (x - d) % 9) continue;
            unsigned long long m = (x - d) / 9;
            if (m == 0) continue;
            printf(first ? "%llu" : " %llu", m * 10 + d);
            first = false;
        }
        printf("\n");
    }
}
