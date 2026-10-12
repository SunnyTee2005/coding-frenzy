#include <cstdio>
int main() {
    double h, u, d, f;
    while (scanf("%lf %lf %lf %lf", &h, &u, &d, &f) == 4 && h != 0) {
        double height = 0, fatigue = u * f / 100, climb = u;
        for (int day = 1;; ++day) {
            if (climb > 0) height += climb;
            if (height > h) { printf("success on day %d\n", day); break; }
            height -= d;
            if (height < 0) { printf("failure on day %d\n", day); break; }
            climb -= fatigue;
        }
    }
}
