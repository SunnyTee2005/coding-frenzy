#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    while (n--) {
        int h, m; scanf("%d:%d", &h, &m);
        int t = ((h % 12) * 60 + m);
        int r = (720 - t) % 720;
        int rh = r / 60, rm = r % 60;
        if (rh == 0) rh = 12;
        printf("%02d:%02d\n", rh, rm);
    }
}
