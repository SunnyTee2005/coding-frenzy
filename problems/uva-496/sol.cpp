#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <sstream>
#include <string>
using namespace std;
int main() {
    string la, lb;
    while (getline(cin, la) && getline(cin, lb)) {
        set<long long> a, b;
        long long x;
        istringstream ia(la), ib(lb);
        while (ia >> x) a.insert(x);
        while (ib >> x) b.insert(x);
        set<long long> common;
        set_intersection(a.begin(), a.end(), b.begin(), b.end(), inserter(common, common.begin()));
        if (a == b) cout << "A equals B\n";
        else if (common.size() == a.size()) cout << "A is a proper subset of B\n";
        else if (common.size() == b.size()) cout << "B is a proper subset of A\n";
        else if (common.empty()) cout << "A and B are disjoint\n";
        else cout << "I'm confused!\n";
    }
}
