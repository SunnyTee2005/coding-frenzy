#include <algorithm>
#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        long long s[4];
        for (int i = 0; i < 4; ++i) scanf("%lld", &s[i]);
        std::sort(s, s + 4);
        if (s[0] == s[3]) puts("square");
        else if (s[0] == s[1] && s[2] == s[3]) puts("rectangle");
        else if (s[3] < s[0] + s[1] + s[2]) puts("quadrangle");
        else puts("banana");
    }
}
