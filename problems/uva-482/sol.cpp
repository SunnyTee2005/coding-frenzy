#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main() {
    string line;
    getline(cin, line);
    int t = stoi(line);
    for (int c = 0; c < t; ++c) {
        while (getline(cin, line) && line.find_first_not_of(" \t\r") == string::npos) {}
        vector<int> p;
        { istringstream in(line); int x; while (in >> x) p.push_back(x); }
        getline(cin, line);
        vector<string> v;
        { istringstream in(line); string x; while (in >> x) v.push_back(x); }
        vector<string> out(p.size());
        for (size_t i = 0; i < p.size(); ++i) out[p[i] - 1] = v[i];
        if (c) cout << "\n";
        for (const string& s : out) cout << s << "\n";
    }
}
