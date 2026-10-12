#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int n, a[1005]; scanf("%d", &n);
        for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
        int s = 0;
        for (int i = 1; i < n; ++i) for (int k = 0; k < i; ++k) if (a[k] <= a[i]) ++s;
        printf("%d\n", s);
    }
}
