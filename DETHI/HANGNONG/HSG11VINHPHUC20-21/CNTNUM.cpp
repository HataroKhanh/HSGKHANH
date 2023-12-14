#include <bits/stdc++.h>
using namespace std;
bool cnt(int &c, int &d, int &x) { return (x % c != 0) && (x % d != 0); }
int main(int argc, char *argv[]) {
  int a, b, c, d, dem = 0;
  cin >> a >> b >> c >> d;

  for (int i = a; i <= b; i++) {
    if (cnt(c, d, i)) {
      dem++;
    }
  }
  cout << dem;
  return 0;
}
