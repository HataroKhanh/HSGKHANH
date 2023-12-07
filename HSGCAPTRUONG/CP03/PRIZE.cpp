#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;
unordered_map<char, int> strings(string &s) {
  unordered_map<char, int> a;
  for (char &i : s) {
    a[i]++;
  }
  return a;
}
bool istrung(unordered_map<char, int> &s, unordered_map<char, int> a) {
  for (int i = 0; i < a.size(); i++) {
    if (s[i] == 0 && a[i] != 0) {
      return false;
    }
  }
  return true;
}
int main(int argc, char *argv[]) {
  string s;
  int n;
  cin >> s >> n;
  vector<unordered_map<char, int>> ss;
  unordered_map<char, int> a;
  for (char &i : s) {
    a[i]++;
  }

  for (int i = 0; i < n; i++) {
    string ip;
    cin >> ip;
    ss.push_back(strings(ip));
  }
  int d = 0;

  for (unordered_map<char, int> &i : ss) {
    if (istrung(i, a)) {
      d++;
    };
  }
  cout << d;

  return 0;
}
