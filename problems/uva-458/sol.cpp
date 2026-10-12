#include <cstdio>
int main() {
    int c;
    while ((c = getchar()) != EOF) putchar(c == '\n' ? c : c - 7);
}
