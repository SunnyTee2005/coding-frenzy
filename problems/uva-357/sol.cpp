#include <cstdio>
long long ways[30001];
int main() {
    const int coins[] = {1, 5, 10, 25, 50};
    ways[0] = 1;
    for (int c : coins) for (int v = c; v <= 30000; ++v) ways[v] += ways[v - c];
    int n;
    while (scanf("%d", &n) == 1) {
        if (ways[n] == 1) printf("There is only 1 way to produce %d cents change.\n", n);
        else printf("There are %lld ways to produce %d cents change.\n", ways[n], n);
    }
}
