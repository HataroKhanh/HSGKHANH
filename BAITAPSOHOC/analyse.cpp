#include <bits/stdc++.h>
#include <vector>
#define ll long long
using namespace std;

ll songuyento(ll &n) {
  if (n <= 1)
    return false;
  for (ll i = 3; i * i < n; i++) {
    if (n % i == 0)
      return false;
  }
  return true;
}
map<int, int> khanh(ll &n) {
  map<int, int> k;
  for (ll i = 2; i <= n; i++) {
    ll j = i, d = 2;
    while (j != 1) {
      if (songuyento(d) && j % d == 0) {
        k[d]++;
        j /= d;
      } else {
        d++;
      }
    }
  }
  return k;
}

int main(int argc, char *argv[]) {
  ll n;

  while (cin >> n) {
    map<int, int> k = khanh(n);
    for (auto &i : k) {
      cout << i.second << " ";
    }
    cout << '\n';
  }
  return 0;
}
