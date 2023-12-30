#include <bits/stdc++.h>
using namespace std;
bool ss(pair<int, int> a, pair<int, int> b) { return a.first < b.first; }
int main() {
  // freopen("DRAGON.INP","r",stdin);
  // freopen("DRAGON.OUT","w",stdout);
  int s, n;
  cin >> s >> n;
  pair<int, int> khanh[n];
  /*  17 6
      48 17
      39 15
      13 3
      32 41
      13 4
      46 14*/

  for (int i = 0; i < n; i++) {
    cin >> khanh[i].first >> khanh[i].second;
  }
  sort(khanh, khanh + n, ss);
  int i = 0;
  int d = 0;
  for (int i = 0; i < n; i++) {
    if (s > khanh[i].first) {
      s += khanh[i].second;
    } else
      d++;
  }

  if (d != 0)
    cout << "NO\n" << d;
  else
    cout << "YES";

  return 0;
}
