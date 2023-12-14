#include <bits/stdc++.h>
#include <climits>
using namespace std;
int main() {

  int n;
  cin >> n;
  int a[n];
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
  }

  int i = 1, j = 2, smax = INT_MIN;
  while (j <= n) {
    smax = max(smax, a[i] + a[j]);
    i++;
    j++;
  }
  cout << smax;
  return 0;
}
