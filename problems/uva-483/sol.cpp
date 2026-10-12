#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
int main() {
    string line;
    while (getline(cin, line)) {
        size_t i = 0;
        while (i < line.size()) {
            if (line[i] == ' ') { ++i; continue; }
            size_t j = i;
            while (j < line.size() && line[j] != ' ') ++j;
            reverse(line.begin() + i, line.begin() + j);
            i = j;
        }
        cout << line << "\n";
    }
}
