#include <cstdio>
#include <cstring>
struct Op { char cmd[3]; int a, x[12]; } ops[1000];
int main() {
    int r, c, cs = 0;
    while (scanf("%d %d", &r, &c) == 2 && (r || c)) {
        int n; scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%2s", ops[i].cmd);
            if (strcmp(ops[i].cmd, "EX") == 0) { ops[i].a = 4; for (int j = 0; j < 4; ++j) scanf("%d", &ops[i].x[j]); }
            else { scanf("%d", &ops[i].a); for (int j = 0; j < ops[i].a; ++j) scanf("%d", &ops[i].x[j]); }
        }
        if (cs) printf("\n");
        printf("Spreadsheet #%d\n", ++cs);
        int q; scanf("%d", &q);
        while (q--) {
            int r0, c0; scanf("%d %d", &r0, &c0);
            int rr = r0, cc = c0;
            bool gone = false;
            // 逐一套用操作，只追蹤這一格的位置
            for (int i = 0; i < n && !gone; ++i) {
                Op& o = ops[i];
                if (strcmp(o.cmd, "EX") == 0) {
                    if (rr == o.x[0] && cc == o.x[1]) { rr = o.x[2]; cc = o.x[3]; }
                    else if (rr == o.x[2] && cc == o.x[3]) { rr = o.x[0]; cc = o.x[1]; }
                    continue;
                }
                bool row = o.cmd[1] == 'R', del = o.cmd[0] == 'D';
                int& v = row ? rr : cc;
                int shift = 0;
                for (int j = 0; j < o.a; ++j) {
                    if (del && o.x[j] == v) gone = true;
                    if (del ? o.x[j] < v : o.x[j] <= v) ++shift;
                }
                v += del ? -shift : shift;
            }
            if (gone) printf("Cell data in (%d,%d) GONE\n", r0, c0);
            else printf("Cell data in (%d,%d) moved to (%d,%d)\n", r0, c0, rr, cc);
        }
    }
}
