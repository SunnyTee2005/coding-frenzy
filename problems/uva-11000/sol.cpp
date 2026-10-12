#include <cstdio>
int main() {
    int n;
    while (scanf("%d", &n) == 1 && n >= 0) {
        long long male = 0, female = 1;
        for (int i = 0; i < n; ++i) {
            long long m = male + female, f = male + 1;
            male = m; female = f;
        }
        printf("%lld %lld\n", male, male + female);
    }
}
