#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(int argc, char *argv[]) {
  ll n, k;
  cin >> n >> k;
  ll a[n + 1];
  unordered_map<int, int> b;
  for (ll i = 1; i <= n; i++) {
    cin >> a[i];
  }

  ll i = 1, j = 1, ssum = 0;
  for (ll i = 1; i <= n; i++) {
    ssum += a[i];
    if (ssum % k == 0) {
      for (ll j = 1; j <= i; j++) {
        cout << a[j] << " ";
      }
      cout << '\n';
    }
    if (b[ssum - k] != 0) {
      for (ll j = b[ssum - k] + 1; j <= i; j++) {
        cout << a[j] << ' ';
      }
      cout << '\n';
    }
    b[ssum] = i;
  }
  return 0;
}
