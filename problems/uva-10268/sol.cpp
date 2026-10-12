#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main() {
    string xl, al;
    while (getline(cin, xl) && getline(cin, al)) {
        long long x = stoll(xl);
        vector<long long> a;
        istringstream in(al);
        long long v;
        while (in >> v) a.push_back(v);
        long long n = (long long)a.size() - 1, r = 0;
        for (long long i = 0; i < n; ++i) r = r * x + a[i] * (n - i);
        cout << r << "\n";
    }
}
