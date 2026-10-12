#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    int n; cin >> n;
    vector<string> st;
    string op, name;
    while (n-- && cin >> op) {
        if (op == "Sleep") { cin >> name; st.push_back(name); }
        else if (op == "Kick") { if (!st.empty()) st.pop_back(); }
        else cout << (st.empty() ? "Not in a dream" : st.back()) << "\n";
    }
}
