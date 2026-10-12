#include <cstdio>
int main() {
    // 每分鐘費率（分），依時段：日 8-18、晚 18-22、夜 22-8
    const int rate[5][3] = {{10, 6, 2}, {25, 15, 5}, {53, 33, 13}, {87, 47, 17}, {144, 80, 30}};
    char step[4], num[16];
    int h1, m1, h2, m2;
    while (scanf("%3s", step) == 1 && step[0] != '#') {
        scanf("%15s %d %d %d %d", num, &h1, &m1, &h2, &m2);
        int t = h1 * 60 + m1, end = h2 * 60 + m2;
        int len = (end - t + 1440) % 1440;
        if (len == 0) len = 1440;
        int mins[3] = {};
        for (int i = 0; i < len; ++i) {
            int m = (t + i) % 1440;
            if (m >= 480 && m < 1080) ++mins[0];
            else if (m >= 1080 && m < 1320) ++mins[1];
            else ++mins[2];
        }
        int s = step[0] - 'A';
        int cents = mins[0] * rate[s][0] + mins[1] * rate[s][1] + mins[2] * rate[s][2];
        printf("%10s%6d%6d%6d%3c%5d.%02d\n", num, mins[0], mins[1], mins[2], step[0], cents / 100, cents % 100);
    }
}
