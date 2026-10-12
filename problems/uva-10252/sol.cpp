#include <iostream>
#include <string>
using namespace std;
int main() {
    string a, b;
    while (getline(cin, a) && getline(cin, b)) {
        int ca[26] = {}, cb[26] = {};
        for (char c : a) if (c >= 'a' && c <= 'z') ++ca[c - 'a'];
        for (char c : b) if (c >= 'a' && c <= 'z') ++cb[c - 'a'];
        string out;
        for (int i = 0; i < 26; ++i) out += string(min(ca[i], cb[i]), char('a' + i));
        cout << out << "\n";
    }
}
