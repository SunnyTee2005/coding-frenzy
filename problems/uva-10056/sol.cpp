#include <cmath>
#include <cstdio>
int main() {
    int s; scanf("%d", &s);
    while (s--) {
        int n, i; double p; scanf("%d %lf %d", &n, &p, &i);
        double q = 1 - p;
        printf("%.4f\n", p * pow(q, i - 1) / (1 - pow(q, n)));
    }
}
