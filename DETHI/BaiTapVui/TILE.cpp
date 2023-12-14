#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll tile(ll n) {
  ll a[100001];
  a[0] = 0;
  a[1] = 1;
  a[2] = 3;
  for (ll i = 3; i <= n; i++) {
    a[i] = 2 * a[i - 2] + a[i - 1];
  }
  return a[n];
}
int main() {
  ll n;
  while (cin >> n) {
    cout << tile(n) << endl;
  }
  return 0;
}
