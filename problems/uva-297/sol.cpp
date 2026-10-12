#include <cstdio>
#include <cstring>
char s[2000];
bool img[32][32];
int pos;
void draw(int r, int c, int size) {
    char ch = s[pos++];
    if (ch == 'p') {
        int h = size / 2;
        draw(r, c + h, h); draw(r, c, h); draw(r + h, c, h); draw(r + h, c + h, h);
    } else if (ch == 'f') {
        for (int i = r; i < r + size; ++i) for (int j = c; j < c + size; ++j) img[i][j] = true;
    }
}
int main() {
    int n; scanf("%d", &n);
    while (n--) {
        memset(img, 0, sizeof img);
        for (int t = 0; t < 2; ++t) { scanf("%s", s); pos = 0; draw(0, 0, 32); }
        int cnt = 0;
        for (int i = 0; i < 32; ++i) for (int j = 0; j < 32; ++j) cnt += img[i][j];
        printf("There are %d black pixels.\n", cnt);
    }
}
