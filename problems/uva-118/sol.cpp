#include <iostream>
#include <string>
using namespace std;
int main() {
    int mx, my; cin >> mx >> my;
    bool scent[55][55] = {};
    const string D = "NESW";
    const int dx[] = {0, 1, 0, -1}, dy[] = {1, 0, -1, 0};
    int x, y; char o; string cmd;
    while (cin >> x >> y >> o >> cmd) {
        int d = (int)D.find(o);
        bool lost = false;
        for (char c : cmd) {
            if (c == 'L') d = (d + 3) % 4;
            else if (c == 'R') d = (d + 1) % 4;
            else {
                int nx = x + dx[d], ny = y + dy[d];
                if (nx < 0 || ny < 0 || nx > mx || ny > my) {
                    if (scent[x][y]) continue;
                    scent[x][y] = true;
                    lost = true;
                    break;
                }
                x = nx; y = ny;
            }
        }
        cout << x << " " << y << " " << D[d] << (lost ? " LOST" : "") << "\n";
    }
}
