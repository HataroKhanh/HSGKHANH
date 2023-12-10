#include <bits/stdc++.h>
#include <climits>
#define N 1000001
int t[N], p[N], dp[N];

using namespace std;
int main() {

  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> t[i];
  }

  for (int i = 1; i <= n - 1; i++) {
    cin >> p[i];
  }

  dp[0] = 0;
  dp[1] = t[1];
  int smin = INT_MAX;
  for (int i = 2; i <= n; i++) {
    dp[i] = min(dp[i - 1] + t[i], dp[i - 2] + p[i - 1]);
  }
  cout << dp[n];

  return 0;
}
