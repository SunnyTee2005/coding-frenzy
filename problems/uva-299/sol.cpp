#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    while (n--) {
        int l, a[55]; scanf("%d", &l);
        for (int i = 0; i < l; ++i) scanf("%d", &a[i]);
        int s = 0;
        for (int i = 0; i < l; ++i) for (int j = i + 1; j < l; ++j) if (a[i] > a[j]) ++s;
        printf("Optimal train swapping takes %d swaps.\n", s);
    }
}
