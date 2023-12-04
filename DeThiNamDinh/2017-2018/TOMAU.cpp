#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;
unordered_map<char, int> DEMSO(string &s) {
  int X = 0, D = 0, V = 0;
  unordered_map<char, int> k;
  for (char i : s) {
    if (i == 'V')
      k['V']++;
    else if (i == 'D')
      k['D']++;
    else if (i == 'X')
      k['X']++;
  }
  return k;
}
// D>X
// X>V
// V>D
int TOMAU(string &s, unordered_map<char, int> &k) {
  return min(k['V'] + k['X'] * 2,
             min(k['X'] + k['D'] * 2, k['D'] + k['V'] * 2));
}
int main() {
  int n;
  string s;
  cin >> n;
  vector<int> a;
  for (int i = 0; i < n; i++) {
    cin >> s;
    unordered_map<char, int> k = DEMSO(s);
    a.push_back(TOMAU(s, k));
  }
  for (int &i : a) {
    cout << i << '\n';
  }

  return 0;
}
