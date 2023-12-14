#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[]) {

  int a, b;
  cin >> a >> b;
  int ssum = a + b;
  cout << ssum << '\n';
  string s = to_string(ssum);
  int smax = -1;
  for (const char &i : s) {
    smax = max(smax, i - '0');
  }
  cout << smax;
  return 0;
}
