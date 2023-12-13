#include <bits/stdc++.h>
#include <vector>
#define ll long long
using namespace std;
ll fa(ll &n) {
  ll k = 1;
  for (ll i = 1; i <= n; i++) {
    k *= i;
  }
  return k;
}
vector<ll> sannguyento() {
  vector<ll> san(10e6, 1);
  san[0] = san[1] = 0;

  for (ll i = 2; i < 1e6; i++) {
    if (san[i] == 1) {
      for (ll j = i * i; j < 1e6; j += i) {
        san[j] = 0;
      }
    }
  }
  return san;
}
void khanh(ll &n, vector<ll> san) {
  vector<ll> k;
  ll dem = 0, i = 0;
  while (1) {
    while (san[i] != 1) {
      i++;
    }
    if (n % i == 0) {
      dem++;
      n /= i;
    } else {
      i++;
      cout << dem << ' ';
      dem = 0;
    }
    if (n == 1)
      break;
  }
  cout << 1 << '\n';
}
int main(int argc, char *argv[]) {
  ll n;
  vector<ll> san = sannguyento();
  while (cin >> n) {
    ll k = fa(n);
    khanh(k, san);
  }
  return 0;
}
