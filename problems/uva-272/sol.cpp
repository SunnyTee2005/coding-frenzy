#include <cstdio>

int main() {
    int c;
    bool open = true;
    while ((c = getchar()) != EOF) {
        if (c == '"') {
            fputs(open ? "``" : "''", stdout);
            open = !open;
        } else {
            putchar(c);
        }
    }
    return 0;
}
