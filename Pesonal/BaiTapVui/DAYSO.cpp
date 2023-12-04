#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  vector<int> aa(n);
  for (int i = 0; i < n; i++) {
    cin >> aa[i];
  }

  vector<int> A(n), B(n);
  A[0] = aa[0];
  for (int i = 1; i < n; i++) {
    A[i] = max(aa[i], A[i - 1]);
  }

  B[n - 1] = aa[n - 1];
  for (int i = n - 2; i >= 0; i--) {
    B[i] = min(aa[i], B[i + 1]);
  }

  int smax = INT_MIN;
  for (int i = 1; i < n - 1; i++) {
    smax = max(smax, A[i - 1] + aa[i] - B[i + 1]);
  }

  cout << smax;
  return 0;
}
