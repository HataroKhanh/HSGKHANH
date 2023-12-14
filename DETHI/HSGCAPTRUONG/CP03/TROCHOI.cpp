#include <bits/stdc++.h>
#include <cmath>
#include <unordered_map>
using namespace std;
int main(int argc, char *argv[]) {

  int n, k;
  cin >> n >> k;

  unordered_map<int, int> a;
  for (int i = 0; i < n; i++) {
    int ip;
    cin >> ip;
    a[ip]++;
  }
  int b[k];
  for (int i = 0; i < k; i++)
    cin >> b[i];

  int smax = 1, d = 1, sdem = 0;
  for (int i = 0; i < k; i++) {
    if (a[b[i]] != 0) {
      sdem += d;
      smax = max(smax, sdem);
      d++;
    } else {
      sdem = 0;
      d = 1;
    }
  }
  cout << smax;
  return 0;
}
