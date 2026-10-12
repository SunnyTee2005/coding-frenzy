#include <cstdio>
#include <vector>
int main() {
    const int N = 1000000;
    std::vector<bool> comp(N + 1, false);
    comp[0] = comp[1] = true;
    for (int i = 2; (long long)i * i <= N; ++i)
        if (!comp[i]) for (int j = i * i; j <= N; j += i) comp[j] = true;
    int n;
    while (scanf("%d", &n) == 1 && n) {
        bool found = false;
        for (int a = 3; a <= n / 2; a += 2)
            if (!comp[a] && !comp[n - a]) { printf("%d = %d + %d\n", n, a, n - a); found = true; break; }
        if (!found) puts("Goldbach's conjecture is wrong.");
    }
}
