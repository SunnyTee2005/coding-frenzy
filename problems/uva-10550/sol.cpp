#include <cstdio>
int main() {
    int a, b, c, d;
    while (scanf("%d %d %d %d", &a, &b, &c, &d) == 4 && (a || b || c || d)) {
        // 順時針轉時刻度往下數，逆時針轉時往上數；每格 9 度
        int marks = 80 + (a - b + 40) % 40 + 40 + (c - b + 40) % 40 + (c - d + 40) % 40;
        printf("%d\n", marks * 9);
    }
}
