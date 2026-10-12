#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
int main() {
    int g; string s;
    while (cin >> g && g) {
        cin >> s;
        size_t len = s.size() / g;
        for (size_t i = 0; i < s.size(); i += len) reverse(s.begin() + i, s.begin() + i + len);
        cout << s << "\n";
    }
}
