#include <cstdio>
#include <vector>
int main() {
    int n;
    while (scanf("%d", &n) == 1) {
        std::vector<int> a(n);
        for (int &x : a) scanf("%d", &x);
        long long inv = 0;
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                if (a[i] > a[j]) ++inv;
        printf("Minimum exchange operations : %lld\n", inv);
    }
}
