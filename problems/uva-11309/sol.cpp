#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
int main() {
    int n; scanf("%d", &n);
    while (n--) {
        int h, m; scanf("%d:%d", &h, &m);
        int t = h * 60 + m;
        for (;;) {
            t = (t + 1) % 1440;
            string s = to_string((t / 60) * 100 + t % 60);
            string r = s; reverse(r.begin(), r.end());
            if (s == r) break;
        }
        printf("%02d:%02d\n", t / 60, t % 60);
    }
}
