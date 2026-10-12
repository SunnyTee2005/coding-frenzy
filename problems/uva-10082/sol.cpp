#include <cstdio>
#include <cstring>
int main() {
    const char* kb = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./";
    int c;
    while ((c = getchar()) != EOF) {
        const char* p = c ? strchr(kb, c) : nullptr;
        putchar(p && p > kb ? p[-1] : c);
    }
}
