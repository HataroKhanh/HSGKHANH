#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll giaithua(ll n) {
  ll ssum = 1;
  for (ll i = 1; i <= n; i++) {
    ssum *= i;
  }
  return ssum;
}
ll tohop(ll n) { return (giaithua(n)) / (giaithua(n - 2) * giaithua(2)); }

int main(int argc, char *argv[]) {
  int n, k;
  cin >> n >> k;
  ll sdem = 0;
  ll a[n];
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
  }

  sort(a + 1, a + n + 1);

  for (int i = 1; i <= n; i++) {
    ll db = lower_bound(a + i, a + n + 1, a[i] + k) - (a + i + 1);
    sdem += tohop(db);
  }
  cout << sdem;

  return 0;
}
