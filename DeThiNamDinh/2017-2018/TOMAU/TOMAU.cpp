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
  int smax = max(k['V'], max(k['X'], k['D']));
  if (smax == k['V']) {
    return k['X'] + k['D'] * 2;
  } else if (smax == k['D']) {
    return k['V'] + k['X'] * 2;
  } else if (smax == k['X']) {
    return k['D'] + k['V'] * 2;
  }
}
int main() {
  int n;
  string s;
  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> s;
    unordered_map<char, int> k = DEMSO(s);
    cout << TOMAU(s, k);
  }

  return 0;
}
