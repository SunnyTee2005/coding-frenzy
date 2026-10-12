#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
int dp[1005][1005];
int main() {
    string a, b;
    while (getline(cin, a) && getline(cin, b)) {
        for (size_t i = 1; i <= a.size(); ++i)
            for (size_t j = 1; j <= b.size(); ++j)
                dp[i][j] = a[i - 1] == b[j - 1] ? dp[i - 1][j - 1] + 1 : max(dp[i - 1][j], dp[i][j - 1]);
        cout << dp[a.size()][b.size()] << "\n";
    }
}
