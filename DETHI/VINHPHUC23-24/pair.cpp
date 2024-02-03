#include <algorithm>
#include <bits/stdc++.h>
#include <vector>
using namespace std;
#define ll long long
ll n, kk, dem = 0;
bool nt(ll &n) {
  if (n <= 1)
    return false;
  else {
    for (ll i = 2; i * i <= n; i++) {
      if (n % i == 0)
        return false;
    }
    return true;
  }
}
vector<ll> nguyent(ll &n) {
  vector<ll> khanh;
  for (ll i = 2; i <= n; i++) {
    if (nt(i)) {
      khanh.push_back(i);
    }
  }
  return khanh;
}
int main(int argc, char *argv[]) {
  cin >> n >> kk;
  vector<ll> k = nguyent(n);

  for (ll i = 0; i < k.size(); i++) {
    ll db = lower_bound(k.begin(), k.end(), k[i] + kk) - k.begin();
    if (k[db] - k[i] == kk) {
      dem++;
    }
  }
  cout << dem;

  return 0;
}
