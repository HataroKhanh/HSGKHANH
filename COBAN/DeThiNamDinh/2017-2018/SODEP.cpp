#include <bits/stdc++.h>
#define ll long long
using namespace std;
bool sodep(ll a) {
  int k = 0;
  for (int i = 1; i <= a; i++) {
    if (a % i == 0) {
      k++;
    }
  }
  return a % k == 0;
}
int main(int argc, char *argv[]) {

  ll a;
  cin >> a;
  if (sodep(a))
    cout << "CO";
  else
    cout << "KHONG";
  return 0;
}
