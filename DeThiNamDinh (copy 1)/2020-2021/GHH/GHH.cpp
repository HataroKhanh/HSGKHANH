#include <bits/stdc++.h>
using namespace std;
bool ghh(int a) {
  int k = 0;
  for (int i = 1; i <= a; i++) {
    if (a % i == 0) {
      k += i;
    }
  }
  // cout << k << '\n';
  return a * 2 <= k;
}
int main(int argc, char *argv[]) {

  int n, d = 0;
  cin >> n;
  int a[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    if (ghh(a[i]))
      d++;
  }
  cout << d << '\n';
  for (int i = 0; i < n; i++) {
    if (ghh(a[i])) {
      cout << a[i] << '\n';
    }
  }

  return 0;
}
