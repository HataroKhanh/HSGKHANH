#include <bits/stdc++.h>
using namespace std;
int main(int argc, char *argv[]) {
  int a, b;
  cin >> a >> b;

  int smax = 0;
  for (int i = 1; i <= 2; i++) {
    if (a >= b) {
      smax += a;
      a--;
    } else {
      smax += b;
      b--;
    }
  }
  cout << smax;

  return 0;
}
