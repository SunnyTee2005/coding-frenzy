#include <cstdio>
#include <cstring>
int main() {
    int m; scanf("%d", &m);
    while (m--) {
        int n, k; scanf("%d %d", &n, &k);
        bool genuine[105] = {};
        int light[105] = {}, heavy[105] = {}, unequal = 0;
        while (k--) {
            int p, left[105], right[105]; char res[4];
            scanf("%d", &p);
            for (int i = 0; i < p; ++i) scanf("%d", &left[i]);
            for (int i = 0; i < p; ++i) scanf("%d", &right[i]);
            scanf("%3s", res);
            if (res[0] == '=') {
                for (int i = 0; i < p; ++i) genuine[left[i]] = genuine[right[i]] = true;
                continue;
            }
            ++unequal;
            bool in[105] = {};
            for (int i = 0; i < p; ++i) in[left[i]] = in[right[i]] = true;
            for (int c = 1; c <= n; ++c) if (!in[c]) genuine[c] = true;  // 沒上秤的一定是真幣
            int* lo = res[0] == '<' ? left : right;
            int* hi = res[0] == '<' ? right : left;
            for (int i = 0; i < p; ++i) { ++light[lo[i]]; ++heavy[hi[i]]; }
        }
        int found = 0, cnt = 0;
        for (int c = 1; c <= n; ++c)
            if (!genuine[c] && (light[c] == unequal || heavy[c] == unequal)) { found = c; ++cnt; }
        printf("%d\n", cnt == 1 ? found : 0);
        if (m) printf("\n");
    }
}
