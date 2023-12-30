
#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  vector<int> k(n);

  for (int i = 0; i < n; i++) {
    cin >> k[i];
  }

  sort(k.rbegin(), k.rend());
  int d = 0;
  for (int i = 0; i < n; i++) {
    d += (k[i] > 0) ? k[i] : 0;
    for (int j = i + 1; j < n; j++) {
      k[j] = k[j] - 1;
    }
  }
  cout << d;

  return 0;
}
