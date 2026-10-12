#include <cctype>
#include <cstdio>
#include <cstring>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        char s[128]; scanf("%s", s);
        double sum = 0;
        for (int i = 0; s[i];) {
            char e = s[i++];
            int n = 0;
            while (isdigit((unsigned char)s[i])) n = n * 10 + (s[i++] - '0');
            if (n == 0) n = 1;
            double w = e == 'C' ? 12.01 : e == 'H' ? 1.008 : e == 'O' ? 16.00 : 14.01;
            sum += w * n;
        }
        printf("%.3f\n", sum);
    }
}
