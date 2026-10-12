#include <cstdio>
int main() {
    const int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    const char* names[] = {"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};  // 2011/1/1 是星期六
    int t; scanf("%d", &t);
    while (t--) {
        int m, d; scanf("%d %d", &m, &d);
        int n = d - 1;
        for (int i = 0; i < m - 1; ++i) n += days[i];
        puts(names[n % 7]);
    }
}
