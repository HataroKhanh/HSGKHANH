#include <bits/stdc++.h>
using namespace std;
int khanh(int a) {
  if (a % 10 != 0) {
    return a % 10;
  } else {
    while (1) {
      a /= 10;
      if (a % 10 != 0) {
        return a % 10;
      }
    }
  }
}
int main() {
  int a;
  cin >> a;
  int d = 0;
  while (a != 0) {
    a -= khanh(a);
    d++;
  }
  cout << d;
  return 0;
}
