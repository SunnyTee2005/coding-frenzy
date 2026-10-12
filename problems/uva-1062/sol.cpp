#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    string s;
    int cs = 0;
    while (cin >> s && s != "end") {
        // 貪心：放到最左邊、頂端字母 >= 它的堆上，否則開新堆
        vector<char> tops;
        for (char c : s) {
            size_t i = 0;
            while (i < tops.size() && tops[i] < c) ++i;
            if (i == tops.size()) tops.push_back(c);
            else tops[i] = c;
        }
        cout << "Case " << ++cs << ": " << tops.size() << "\n";
    }
}
