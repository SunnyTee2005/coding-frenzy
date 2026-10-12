#include <cstdio>
int a[105][105];
int main() {
    int n;
    while (scanf("%d", &n) == 1 && n) {
        for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) scanf("%d", &a[i][j]);
        int br = 0, bc = 0, r = -1, c = -1;
        for (int i = 0; i < n; ++i) {
            int s = 0, t = 0;
            for (int j = 0; j < n; ++j) { s += a[i][j]; t += a[j][i]; }
            if (s % 2) { ++br; r = i; }
            if (t % 2) { ++bc; c = i; }
        }
        if (br == 0 && bc == 0) puts("OK");
        else if (br == 1 && bc == 1) printf("Change bit (%d,%d)\n", r + 1, c + 1);
        else puts("Corrupt");
    }
}
