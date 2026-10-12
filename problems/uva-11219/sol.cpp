#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    for (int c = 1; c <= t; ++c) {
        int cd, cm, cy, bd, bm, by;
        scanf("%d/%d/%d %d/%d/%d", &cd, &cm, &cy, &bd, &bm, &by);
        int age = cy - by;
        if (cm < bm || (cm == bm && cd < bd)) --age;
        printf("Case #%d: ", c);
        if (age < 0) puts("Invalid birth date");
        else if (age > 130) puts("Check birth date");
        else printf("%d\n", age);
    }
}
