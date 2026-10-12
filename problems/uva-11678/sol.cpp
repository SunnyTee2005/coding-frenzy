#include <algorithm>
#include <cstdio>
#include <set>
using namespace std;
int main() {
    int a, b;
    while (scanf("%d %d", &a, &b) == 2 && (a || b)) {
        set<int> sa, sb;
        for (int i = 0; i < a; ++i) { int x; scanf("%d", &x); sa.insert(x); }
        for (int i = 0; i < b; ++i) { int x; scanf("%d", &x); sb.insert(x); }
        int onlyA = 0, onlyB = 0;
        for (int x : sa) if (!sb.count(x)) ++onlyA;
        for (int x : sb) if (!sa.count(x)) ++onlyB;
        printf("%d\n", min(onlyA, onlyB));
    }
}
