#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
int main(int argc, char *argv[]) {

  int n, k;
  cin >> n >> k;
  int a[n];
  for (int i = 0; i < n; i++)
    cin >> a[i];

  sort(a, a + n);

  int d = upper_bound(a, a + n, k) - a;

  if (a[d] == k)
    cout << "YES\n" << d;
  else
    cout << "NO";
  return 0;
}
