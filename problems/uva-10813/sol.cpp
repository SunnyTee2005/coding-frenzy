#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int card[5][5];
        bool mark[5][5] = {};
        for (int i = 0; i < 5; ++i)
            for (int j = 0; j < 5; ++j) {
                if (i == 2 && j == 2) { card[i][j] = 0; mark[i][j] = true; continue; }
                scanf("%d", &card[i][j]);
            }
        int ans = 0;
        for (int k = 1; k <= 75; ++k) {
            int x; scanf("%d", &x);
            if (ans) continue;
            for (int i = 0; i < 5; ++i) for (int j = 0; j < 5; ++j) if (card[i][j] == x) mark[i][j] = true;
            bool win = false;
            for (int i = 0; i < 5; ++i) {
                bool r = true, c = true;
                for (int j = 0; j < 5; ++j) { r &= mark[i][j]; c &= mark[j][i]; }
                win |= r || c;
            }
            bool d1 = true, d2 = true;
            for (int i = 0; i < 5; ++i) { d1 &= mark[i][i]; d2 &= mark[i][4 - i]; }
            if (win || d1 || d2) ans = k;
        }
        printf("BINGO after %d numbers announced\n", ans);
    }
}
