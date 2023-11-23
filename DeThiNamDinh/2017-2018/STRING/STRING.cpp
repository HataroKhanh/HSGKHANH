#include <bits/stdc++.h>
using namespace std;
int main(int argc, char *argv[]) {
  string s;
  getline(cin, s);
  vector<string> ms;
  string d = "";
  int dmax = -1;
  for (char i : s) {
    if (i == ' ') {
      if (!d.empty()) {
        ms.push_back(d);
        dmax = max(dmax, (int)d.size());
        d = "";
      }
    } else {
      d += i;
    }
  }
  if (!d.empty()) {
    ms.push_back(d);
    dmax = max(dmax, (int)d.size());
  }
  for (int i = 0; i < ms.size(); i++) {
    if ((int)ms[i].size() == dmax) {
      cout << ms[i];
      return 0;
    }
  }
  return 0;
}
