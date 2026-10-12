#include <iostream>
#include <map>
#include <string>
using namespace std;
bool vowel(char c) { return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'; }
bool ends(const string& w, const string& suf) { return w.size() >= suf.size() && w.compare(w.size() - suf.size(), suf.size(), suf) == 0; }
int main() {
    int l, n; cin >> l >> n;
    map<string, string> irr;
    for (int i = 0; i < l; ++i) { string a, b; cin >> a >> b; irr[a] = b; }
    while (n--) {
        string w; cin >> w;
        if (irr.count(w)) cout << irr[w];
        else if (w.size() >= 2 && w.back() == 'y' && !vowel(w[w.size() - 2])) cout << w.substr(0, w.size() - 1) << "ies";
        else if (ends(w, "o") || ends(w, "s") || ends(w, "ch") || ends(w, "sh") || ends(w, "x")) cout << w << "es";
        else cout << w << "s";
        cout << "\n";
    }
}
