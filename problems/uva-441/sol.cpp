#include <cstdio>
int k, s[15], pick[6];
void go(int from, int d) {
    if (d == 6) {
        for (int i = 0; i < 6; ++i) printf(i ? " %d" : "%d", pick[i]);
        printf("\n");
        return;
    }
    for (int i = from; i < k; ++i) { pick[d] = s[i]; go(i + 1, d + 1); }
}
int main() {
    bool first = true;
    while (scanf("%d", &k) == 1 && k) {
        for (int i = 0; i < k; ++i) scanf("%d", &s[i]);
        if (!first) printf("\n");
        first = false;
        go(0, 0);
    }
}
