#include <cstdio>
#include <cstdlib>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int n, a[20], b[20]; scanf("%d", &n);
        for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
        bool zero = false;
        for (int step = 0; step <= 1000 && !zero; ++step) {
            zero = true;
            for (int i = 0; i < n; ++i) if (a[i]) zero = false;
            if (zero) break;
            for (int i = 0; i < n; ++i) b[i] = abs(a[i] - a[(i + 1) % n]);
            for (int i = 0; i < n; ++i) a[i] = b[i];
        }
        puts(zero ? "ZERO" : "LOOP");
    }
}
