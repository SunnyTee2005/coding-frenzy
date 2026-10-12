#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    puts("Lumberjacks:");
    while (n--) {
        int a[10];
        for (int i = 0; i < 10; ++i) scanf("%d", &a[i]);
        bool inc = true, dec = true;
        for (int i = 1; i < 10; ++i) {
            if (a[i] < a[i - 1]) inc = false;
            if (a[i] > a[i - 1]) dec = false;
        }
        puts(inc || dec ? "Ordered" : "Unordered");
    }
}
