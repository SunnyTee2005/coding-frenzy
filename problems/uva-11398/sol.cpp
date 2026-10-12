#include <iostream>
#include <string>
using namespace std;
int main() {
    string tok;
    int flag = 1;
    long long v = 0;
    while (cin >> tok && tok != "~") {
        if (tok == "#") { cout << v << "\n"; v = 0; flag = 1; }
        else if (tok == "0") flag = 1;
        else if (tok == "00") flag = 0;
        else for (size_t i = 0; i < tok.size() - 2; ++i) v = v * 2 + flag;
    }
}
