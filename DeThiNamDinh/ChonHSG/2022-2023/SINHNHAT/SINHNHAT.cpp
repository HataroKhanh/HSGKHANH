#include <algorithm>
#include <bits/stdc++.h>
#include <functional>
#include <unordered_map>
using namespace std;
int main(int argc, char *argv[]) {
  int n, k;
  cin >> n >> k;
  int a[n], b[n];
  unordered_map<int, int> aa;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    b[i] = a[i];
    aa[a[i]] = 0;
  }
  sort(a, a + n, greater<int>());
  int ssum = 0;
  for (int i = 0; i < k; i++) {
    ssum += a[i];
    aa[a[i]] = 1;
    /* cout << "a[i]";
    cout << a[i] << " ";
    cout << '\n'; */
  }
  /* for (int i : b)
    cout << i << " ";
  cout << "\n"; */
  cout << ssum << '\n';
  for (int i = 0; i < n; i++) {
    if (aa[b[i]] == 1) {
      cout << i + 1 << " ";
    }
  }
  return 0;
}
