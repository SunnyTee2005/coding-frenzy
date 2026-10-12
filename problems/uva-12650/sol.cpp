#include <cstdio>
#include <cstring>
bool back[10005];
int main() {
    int n, r;
    while (scanf("%d %d", &n, &r) == 2) {
        memset(back, 0, sizeof back);
        for (int i = 0; i < r; ++i) { int x; scanf("%d", &x); back[x] = true; }
        if (n == r) { puts("*"); continue; }
        for (int i = 1; i <= n; ++i) if (!back[i]) printf("%d ", i);
        printf("\n");
    }
}
