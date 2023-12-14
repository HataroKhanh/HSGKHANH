#include <bits/stdc++.h>
#include <climits>
using namespace std;
int main(int argc, char *argv[]) {
  int n, xmax = INT_MIN, xmin = INT_MAX, ymax = INT_MIN, ymin = INT_MAX;
  cin >> n;
  pair<int, int> a[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i].first >> a[i].second;
    xmax = max(xmax, a[i].first);
    xmin = min(xmin, a[i].first);
    ymax = max(ymax, a[i].second);
    ymin = min(ymin, a[i].second);
  }

  cout << pow(max(xmax - xmin, ymax - ymin), 2);

  return 0;
}
