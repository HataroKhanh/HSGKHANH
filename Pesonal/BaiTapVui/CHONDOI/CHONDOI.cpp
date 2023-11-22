#include <bits/stdc++.h>
#include <math.h>
#include <string>
using namespace std;
long long b[10], n;
long long t;
string s;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  // freopen("CHONDOI.INP", "r", stdin);
  // freopen("CHONDOI.OUT", "w", stdout);
  cin >> n;
  // cin.ignore(0);
  while (n--) {
    cin >> s;
    if (s[0] == 'H')
      b[1]++;
    if (s[0] == 'S')
      b[2]++;
    if (s[0] == 'G')
      b[3]++;
    if (s[0] == 'P')
      b[4]++;
    if (s[0] == 'T')
      b[5]++;
  }
  t = b[1] * b[2] * b[3] + b[1] * b[2] * b[4] + b[1] * b[2] * b[5] +
      b[1] * b[3] * b[4] + b[1] * b[3] * b[5] + b[1] * b[4] * b[5] +
      b[2] * b[3] * b[4] + b[2] * b[3] * b[5] + b[2] * b[4] * b[5] +
      b[3] * b[4] * b[5];
  cout << t;
  return 0;
}
