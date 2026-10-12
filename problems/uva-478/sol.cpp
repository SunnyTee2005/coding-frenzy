#include <cmath>
#include <cstdio>
#include <vector>
using namespace std;
struct Fig { char t; double v[6]; };
static double cross(double ax, double ay, double bx, double by, double px, double py) {
    return (bx - ax) * (py - ay) - (by - ay) * (px - ax);
}
int main() {
    vector<Fig> f;
    char c;
    while (scanf(" %c", &c) == 1 && c != '*') {
        Fig g; g.t = c;
        int n = c == 'r' ? 4 : c == 'c' ? 3 : 6;
        for (int i = 0; i < n; ++i) scanf("%lf", &g.v[i]);
        f.push_back(g);
    }
    double x, y;
    int id = 0;
    while (scanf("%lf %lf", &x, &y) == 2) {
        if (fabs(x - 9999.9) < 1e-9 && fabs(y - 9999.9) < 1e-9) break;
        ++id;
        bool any = false;
        for (size_t i = 0; i < f.size(); ++i) {
            const double *v = f[i].v;
            bool in = false;
            if (f[i].t == 'r') in = x > v[0] && x < v[2] && y < v[1] && y > v[3];
            else if (f[i].t == 'c') in = (x - v[0]) * (x - v[0]) + (y - v[1]) * (y - v[1]) < v[2] * v[2];
            else {
                double d1 = cross(v[0], v[1], v[2], v[3], x, y), d2 = cross(v[2], v[3], v[4], v[5], x, y), d3 = cross(v[4], v[5], v[0], v[1], x, y);
                in = (d1 > 0 && d2 > 0 && d3 > 0) || (d1 < 0 && d2 < 0 && d3 < 0);
            }
            if (in) { printf("Point %d is contained in figure %zu\n", id, i + 1); any = true; }
        }
        if (!any) printf("Point %d is not contained in any figure\n", id);
    }
}
