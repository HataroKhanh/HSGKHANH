#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  int a[n], b[n], c[n];

  for (int i = 1; i <= n; i++)
    cin >> a[i];
  for (int i = 1; i <= n; i++) {
    if (a[i] == 1) {
      b[i] = b[i - 1] + 1;
    } else {
      b[i] = b[i - 1];
    }
  }

  for (int i = n; i > 0; i--) {
    if (a[i] == 3) {
      c[i] = c[i + 1] + 1;
    } else {
      c[i] = c[i + 1];
    }
  }

  int res = 0;
  for (int i = 1; i = n; i++) {
    if (a[i] == 2) {
    }
  }
  return 0;
}
