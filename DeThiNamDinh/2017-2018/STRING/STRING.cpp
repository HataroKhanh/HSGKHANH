#include <bits/stdc++.h>
#include <string>
using namespace std;

int main(int argc, char *argv[]) {

  string s;
  getline(cin, s);

  vector<string> ms;
  string d = "";

  for (char i : s) {
    d += i;
    if (i == ' ') {
      ms.push_back(d);
      d = "";
    }
  }
  if (d != " ")
    ms.push_back(d);
  // cout << d;
  /* for (int i = 0; i < ms.size(); i++)
    cout << ms[i] << " "; */
  int f = -1;
  for (string i : ms) {
    f = max(f, (int)i.size());
  }
  for (string i : ms) {
    if (i.size() == f) {
      cout << i << " ";
    }
  }

  return 0;
}
