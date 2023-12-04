#include <algorithm>
#include <bits/stdc++.h>
#include <climits>
#include <vector>
using namespace std;
bool khanh(pair<int, int> &a, pair<int, int> &b) {
  return (a.second - a.first) < (b.second - b.first);
}
int main(int argc, char *argv[]) {
  int in;
  int n, k, ip;
  cin >> n >> k;
  vector<int> a(n, 0), b(n, 0);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  for (int i = 0; i < n; i++) {
    b[i] = a[i] + b[i - 1];
  }
  // for(int i:b)cout<<i<<" ";
  pair<int, int> aa[n];
  int smax = INT_MIN;
  for (int i = n; i >= 0; i--) {
    int db = lower_bound(b.begin(), b.end(), b[i] - k) - b.begin();

    if (b[i] - b[db] == k) {
      aa[n - i].first = db;
      aa[n - i].second = i;
    }
    // smax=max(smax);
  }
  auto pmax = max_element(aa, aa + n, khanh);
  // cout << pmax->first << " " << pmax->second;
  for (int i = pmax->first + 1; i <= pmax->second; i++) {
    cout << a[i] << " ";
  }
  return 0;
}
