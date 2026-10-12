#include <cstdio>
#include <deque>

int main() {
    int n;
    while (scanf("%d", &n) == 1 && n) {
        std::deque<int> q;
        for (int i = 1; i <= n; ++i) q.push_back(i);
        printf("Discarded cards:");
        bool first = true;
        while (q.size() > 1) {
            printf(first ? " %d" : ", %d", q.front());
            first = false;
            q.pop_front();
            q.push_back(q.front());
            q.pop_front();
        }
        printf("\nRemaining card: %d\n", q.front());
    }
    return 0;
}
