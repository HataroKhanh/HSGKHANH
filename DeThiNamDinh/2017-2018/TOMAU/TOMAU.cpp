#include <bits/stdc++.h>
using namespace std;
char smax(string &s) {
  int D = 0, V = 0, X = 0;
  {
    for (char i : s) {
      if (i == 'V')
        V++;
      else if (i == 'X')
        X++;
      else if (i == 'D')
        D++;
    }
  }
  int d = max(D, max(V, X));
  if (D == d)
    return 'D';
  else if (V == d)
    return 'V';
  else
    return 'X';
}
int main() {
  // D-->X
  // X-->V
  // V-->D
  // VDVVX -->D>X>V X>V
  // DXVVXD
  int n;
  string s;
  cin >> n;
  vector<string> ss;
  /*   vector<int> ds; */
  for (int i = 0; i < n; i++) {
    cin >> s;
    ss.push_back(s);
  }

  for (int i = 0; i < n; i++) {
    int dem = 0;
    char c = smax(ss[i]);
    /*     cout << "Max: " << c << '\n'; */
    for (char i : ss[i]) {
      if (c == 'V') {
        if (i == 'X')
          dem++;
        else if (i == 'D')
          dem += 2;
      } else if (c == 'X') {
        if (i == 'D')
          dem++;
        else if (i == 'V')
          dem += 2;
      } else if (c == 'D') {
        if (i == 'V')
          dem++;
        else if (i == 'X')
          dem += 2;
      }
    }
    cout << dem << '\n';
  }
  return 0;
}
