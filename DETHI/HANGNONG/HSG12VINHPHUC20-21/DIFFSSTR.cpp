#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;
int main(int argc, char *argv[]) {

  int n, d = 0, smax = INT_MIN;
  string s;

  cin >> n;
  cin >> s;

  for (int i = 0; i < n; i++) {
    map<char, int> a;
    for (int j = i; j < n; j++) {
      if (a[s[j]] == 0) {
        d++;
        a[s[j]]++;
      } else {
        smax = max(smax, d);
        d = 0;
        break;
      }
    }
  }
  cout << smax;
  return 0;
}
