#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        vector<string> name(n); vector<int> freq(n);
        // (時間, 輸入順序)：時間相同時先輸出先輸入的藥
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        for (int i = 0; i < n; ++i) { cin >> name[i] >> freq[i]; pq.push({freq[i], i}); }
        while (k--) {
            auto [tm, i] = pq.top(); pq.pop();
            cout << tm << " " << name[i] << "\n";
            pq.push({tm + freq[i], i});
        }
    }
}
