#include <bits/stdc++.h>
#include <functional>
using namespace std;
int main() {
  int n, k;
  cin >> n >> k;

  int ip;
  vector<int> aa;
  for (int i = 0; i < n; i++) {
    cin >> ip;
    aa.push_back(ip);
  }

  // 4 7
  // 20 15 17 10
  // 15
  // 20-15=5
  // 17-15=2
  sort(aa.begin(), aa.end(), greater<int>());

  return 0;
}
