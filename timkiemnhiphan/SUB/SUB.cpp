
#include <algorithm>
#include <bits/stdc++.h>
#include <climits>
using namespace std;
int main() {
  int n, k;
  cin >> n >> k;
  int a[n], b[n];
  for (int i = 0; i < n; i++)
    cin >> a[i];
  b[0] = a[0];
  for (int i = 0; i < n; i++)
    b[i] = a[i] + b[i - 1];

  int smin = INT_MAX;

  for (int i = 0; i < n; i++) {
    int khanh = lower_bound(b + i, b + n, b[i] + k) - b - i;
    if (b[khanh] == b[i] + k && khanh < n) {
      smin = min(smin, khanh - i);
    }
  }
  cout << ((smin != INT_MAX) ? smin : -1);
  return 0;
}
