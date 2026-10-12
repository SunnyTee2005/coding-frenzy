#include <cstdio>
#include <cstdlib>
int main() {
    int a, b;
    while (scanf("%d %d", &a, &b) == 2 && !(a == -1 && b == -1)) {
        int d = abs(a - b);
        printf("%d\n", d < 100 - d ? d : 100 - d);
    }
}
