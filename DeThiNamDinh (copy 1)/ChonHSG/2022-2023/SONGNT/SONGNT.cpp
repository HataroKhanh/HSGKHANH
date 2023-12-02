#include <bits/stdc++.h>
#include <string>
using namespace std;
bool songnt(const int &n) {
  if (n <= 1)
    return 0;
  else {
    for (int i = 2; i < n; i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }
}
int main() {

  string s;
  while (cin >> s) {
    int a = stoi(s), b = 0;
    // cout << a << '\n';
    for (const char i : s) {
      b += i - '0';
    }
    if (songnt(a) && songnt(b))
      cout << "YES\n";
    else {
      // cout << songnt(a) << " " << songnt(b) << '\n';
      cout << "NO\n";
    }
  }

  return 0;
}
