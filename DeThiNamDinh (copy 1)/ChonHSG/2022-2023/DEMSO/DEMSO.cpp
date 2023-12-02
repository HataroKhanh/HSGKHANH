#include <bits/stdc++.h>
using namespace std;
bool isnum(char &s) {
  if (s == '0' || s == '1' || s == '2' || s == '3' || s == '7' || s == '6' ||
      s == '5' || s == '4' || s == '8' || s == '9')
    return true;
  else {
    return false;
  }
}
int stringa(string &s) {
  int d = 0;
  string ss;
  for (char i : s) {
    if (isnum(i)) {
      ss += i;
    } else {
      if (!ss.empty()) {
        d++;
        ss = "";
      }
    }
  }
  if (!ss.empty())
    d++;
  return d;
}
int main() {
  string s;
  cin >> s;
  cout << stringa(s);
  return 0;
}
