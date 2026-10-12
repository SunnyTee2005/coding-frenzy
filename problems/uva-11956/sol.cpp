#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int main() {
    int t; cin >> t;
    for (int c = 1; c <= t; ++c) {
        string p; cin >> p;
        unsigned char mem[100] = {};
        int ptr = 0;
        for (char ch : p) {
            if (ch == '>') ptr = (ptr + 1) % 100;
            else if (ch == '<') ptr = (ptr + 99) % 100;
            else if (ch == '+') ++mem[ptr];
            else if (ch == '-') --mem[ptr];
        }
        printf("Case %d:", c);
        for (int i = 0; i < 100; ++i) printf(" %02X", mem[i]);
        printf("\n");
    }
}
