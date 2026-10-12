#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
    int c[9];
    while (scanf("%d %d %d %d %d %d %d %d %d", &c[0], &c[1], &c[2], &c[3], &c[4], &c[5], &c[6], &c[7], &c[8]) == 9) {
        string out;
        for (int i = 0; i < 9; ++i) {
            int v = c[i], deg = 8 - i;
            if (!v) continue;
            if (out.empty()) { if (v < 0) out += "-"; }
            else out += v < 0 ? " - " : " + ";
            int a = abs(v);
            if (a != 1 || deg == 0) out += to_string(a);
            if (deg >= 1) out += "x";
            if (deg >= 2) out += "^" + to_string(deg);
        }
        if (out.empty()) out = "0";
        puts(out.c_str());
    }
}
