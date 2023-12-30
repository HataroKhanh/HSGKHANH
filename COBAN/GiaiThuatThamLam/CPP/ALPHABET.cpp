#include <bits/stdc++.h>
#include <vector>
using namespace std;
char siu(int d) { return 'A' + d; }
vector<string> khanh(vector<string> &ss) {
  for (int i = 0; i <= ss.size(); i++) {
    int index = 0;
    for (char &i : ss[i]) {
      index++;
      if (i != '.') {
        break;
      }
    }
    int d = 0;
    for (int i = index - 1; i >= 0; i--) {
      if (ss[i + 1][i] == siu(d)) {
        d++;
      } else {
        d--;
      }
    }
    d = 0;
    for (int i = index + 1; i < ss[i].size(); i++) {
      if (ss[i + 1][i] == siu(d)) {
        d++;
      } else {
        d--;
      }
    }
  }
  return ss;
}
int main() {
  int testcase, col;
  string s;

  cin >> testcase;

  while (testcase--) {
    vector<string> ss;
    cin >> col;
    for (int i = 0; i < col; i++) {
      cin >> s;
      ss.push_back(s);
    }
    vector<string> k = khanh(ss);
    for (string &i : k) {
      cout << i << '\n';
    }
  }
}
