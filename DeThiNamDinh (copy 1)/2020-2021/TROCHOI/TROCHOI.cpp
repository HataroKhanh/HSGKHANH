#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;
int getint(string &s) {
  string a;
  for (const char &i : s) {
    if (i >= '0' && i <= '9') {
      a += i;
    }
  }
  return stoi(a);
}
int main(int argc, char *argv[]) {

  int n;
  string s;
  unordered_map<string, int> a;
  for (int i = 0; i < n; i++) {
    cin >> s;
    a[s] = getint(s);
  }
  sort(a.begin(), a.end());
  for (auto i : a) {
    cout << i.first << '\n';
  }

  return 0;
}
