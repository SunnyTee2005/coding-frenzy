#include <cstdio>
#include <string>
int main() {
    int n; scanf("%d", &n);
    while (n--) {
        unsigned a, b; char op;
        scanf("%x %c %x", &a, &op, &b);
        auto bin = [](unsigned v) { std::string s; for (int i = 12; i >= 0; --i) s += char('0' + ((v >> i) & 1)); return s; };
        int r = op == '+' ? (int)a + (int)b : (int)a - (int)b;
        printf("%s %c %s = %d\n", bin(a).c_str(), op, bin(b).c_str(), r);
    }
}
