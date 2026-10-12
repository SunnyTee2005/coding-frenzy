#include <iostream>
#include <string>
using namespace std;
int main() {
    int n; cin >> n;
    string w;
    while (n-- && cin >> w) {
        if (w.size() == 5) { cout << 3 << "\n"; continue; }
        int same = (w[0] == 'o') + (w[1] == 'n') + (w[2] == 'e');
        cout << (same >= 2 ? 1 : 2) << "\n";
    }
}
