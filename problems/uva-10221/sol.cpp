#include <cmath>
#include <cstdio>
#include <cstring>
int main() {
    double s, a; char unit[8];
    const double PI = acos(-1.0);
    while (scanf("%lf %lf %7s", &s, &a, unit) == 3) {
        if (strcmp(unit, "min") == 0) a /= 60;
        double r = 6440 + s, th = a * PI / 180;
        printf("%.6f %.6f\n", r * th, 2 * r * sin(th / 2));
    }
}
