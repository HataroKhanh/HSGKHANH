#include <bits/stdc++.h>
using namespace std;
int main(int argc, char *argv[]) {
  int n;
  cin >> n;
  int a[n], b[n];
  for (int i = 1; i <= n; i++)
    cin >> a[i];
  b[0] = a[0];
  for (int i = 1; i <= n; i++)
    b[i] = a[i] + b[i - 1];
  int i = 0, j = 1, dem = 0;

  while (j <= n) {
    if ((b[j] - b[i]) % 3 == 0 && i < j) {
      dem++;
      i++;
    } else {
      j++;
    }
  }
  cout << dem;
  return 0;
}
