#include <iostream>
#include <stack>
#include <string>
using namespace std;
int main() {
    int n; cin >> n;
    int rows[26] = {}, cols[26] = {};
    for (int i = 0; i < n; ++i) { char name; int r, c; cin >> name >> r >> c; rows[name - 'A'] = r; cols[name - 'A'] = c; }
    string e;
    while (cin >> e) {
        stack<pair<long long, long long>> st;
        long long cost = 0;
        bool error = false;
        for (char ch : e) {
            if (ch == '(') continue;
            if (ch == ')') {
                auto b = st.top(); st.pop();
                auto a = st.top(); st.pop();
                if (a.second != b.first) { error = true; break; }
                cost += a.first * a.second * b.second;
                st.push({a.first, b.second});
            } else st.push({rows[ch - 'A'], cols[ch - 'A']});
        }
        if (error) cout << "error\n"; else cout << cost << "\n";
    }
}
