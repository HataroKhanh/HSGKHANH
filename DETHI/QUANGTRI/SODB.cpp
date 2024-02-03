
#include <array>
#include <bits/stdc++.h>
#include <string>
#include <tuple>
using namespace std;
#define ll long long
const ll SMAX = 10e6 + 2;
ll n, a[SMAX], sdem = 0;
bool nt(ll n) {
  if (n <= 1)
    return false;
  else {
    for (ll i = 2; i * i <= n; i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }
}
bool lechan(ll n) {
  string t = to_string(n);
  ll le = 0, chan = 0;
  for (char i : t) {
    ll q = i - '0';
    if (q % 2 == 0)
      chan++;
    else
      le++;
  }
  return le != chan;
}
int main(int argc, char *argv[]) {
  cin >> n;
  for (ll i = 1; i <= n; i++)
    cin >> a[i];

  for (ll i = 1; i <= n; i++) {
    if (nt(a[i]) and lechan(a[i]))
      sdem++;
  }
  cout << sdem;
  return 0;
}
