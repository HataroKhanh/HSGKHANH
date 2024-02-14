#include <algorithm>
#include <bits/stdc++.h>
#include <climits>
#include <cmath>
#include <cstdio>
#include <functional>
#define ll long long
using namespace std;
bool khanh(ll h, ll n, ll m, ll a[]) {
  ll ssum = 0;
  for (ll i = 1; i <= n; i++) {
    if (a[i] > h) {
      ssum += a[i] - h;
    }
  }
  if (ssum >= m) {
    return true;
  } else {
    return false;
  }
}
int main(int argc, char *argv[]) {
  ll n, m, smax = 0;

 
  cin >> n >> m;
  ll a[n];
  for (ll i = 1; i <= n; i++) {
    cin >> a[i];
    smax = max(smax, a[i]);
  }
  sort(a + 1, a + n + 1);
  ll i = 0, j = smax, ketqua = 0;
  while (i <= j) {
    ll mid = (i + j) / 2;
    if (khanh(mid, n, m, a)) {

      i = mid + 1;
      ketqua = mid;
    } else {
      j = mid - 1;
    }
  }
  cout << ketqua;
  return 0;
}
