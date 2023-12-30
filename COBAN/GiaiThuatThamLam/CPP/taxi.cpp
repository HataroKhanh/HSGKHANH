
#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, d = 0;
  cin >> n;

  // ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  vector<int> a(4, 0); //

  for (int i = 0; i < n; i++) {
    a[i]++;
  }

  while (!allZeros) // 0 0 0 0
  {
    int t = 0;
    if (a[4] != 0) {
      d++;
      a[4]--;
    }

    if (a[1] != 0 && a[3] != 0) {
      a[1]--, a[3]--;
      d++;
    } else if (a[2] >= 2) {
      d++;
      a[2] -= 2;
    } else {
      int i;
      for (i = 0; i < 3; i++) {
        t += a[i];
        if (t >= 4)
          d += 2;
      }
    }
  }
  cout << d;
  return 0;
}
