#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    string line;
    if (!getline(cin, line)) return 0;
    n = stoi(line);
    while (n--) {
        if (!getline(cin, line)) line.clear();
        if (!line.empty() && line.back() == '\r') line.pop_back();
        string st;
        bool ok = true;
        for (char c : line) {
            if (c == '(' || c == '[') st.push_back(c);
            else if (c == ')' || c == ']') {
                char want = c == ')' ? '(' : '[';
                if (st.empty() || st.back() != want) { ok = false; break; }
                st.pop_back();
            }
        }
        cout << (ok && st.empty() ? "Yes" : "No") << "\n";
    }
    return 0;
}
