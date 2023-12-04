#include <bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;
int khanh(string b) {
  int i;
  for (i = b.size() - 1; i >= 0; i--) {
    if (b[i] != '0') {
      break;
    }
  }
  return b[i] - '0';
}
int main() {
  int a;
  int d = 0;

  cin >> a;
  string b = to_string(a);
  while (a != 0) {
    string b = to_string(a);
    a -= khanh(b);

    d++;
  }
  cout << d;
}
