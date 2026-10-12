#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;
struct Item { long long time; int id, period; bool operator<(const Item& o) const { return time != o.time ? time > o.time : id > o.id; } };
int main() {
    priority_queue<Item> pq;
    char cmd[20];
    while (scanf("%19s", cmd) == 1 && cmd[0] != '#') {
        int id, period; scanf("%d %d", &id, &period);
        pq.push({period, id, period});
    }
    int k; scanf("%d", &k);
    while (k--) {
        Item it = pq.top(); pq.pop();
        printf("%d\n", it.id);
        it.time += it.period;
        pq.push(it);
    }
}
