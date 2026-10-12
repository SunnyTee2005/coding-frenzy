#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    vector<string> dict;
    string w;
    while (cin >> w && w != "XXXXXX") dict.push_back(w);
    sort(dict.begin(), dict.end());
    while (cin >> w && w != "XXXXXX") {
        string key = w; sort(key.begin(), key.end());
        bool any = false;
        for (const string &d : dict) {
            string dk = d; sort(dk.begin(), dk.end());
            if (dk == key) { cout << d << "\n"; any = true; }
        }
        if (!any) cout << "NOT A VALID WORD\n";
        cout << "******\n";
    }
}
