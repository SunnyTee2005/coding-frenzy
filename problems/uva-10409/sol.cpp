#include <iostream>
#include <string>
using namespace std;
int main() {
    int n;
    while (cin >> n && n) {
        int top = 1, north = 2, west = 3, bottom = 6, south = 5, east = 4, tmp;
        while (n--) {
            string c; cin >> c;
            if (c == "north") { tmp = top; top = south; south = bottom; bottom = north; north = tmp; }
            else if (c == "south") { tmp = top; top = north; north = bottom; bottom = south; south = tmp; }
            else if (c == "east") { tmp = top; top = west; west = bottom; bottom = east; east = tmp; }
            else { tmp = top; top = east; east = bottom; bottom = west; west = tmp; }
        }
        cout << top << "\n";
    }
}
