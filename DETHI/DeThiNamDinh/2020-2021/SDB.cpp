#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
  long long n;
  cin >> n;
  int a[n];
  unordered_map<int, int> aa;

  for (long long i = 0; i < n; i++) {
    cin >> a[i];
    aa[a[i]]++;
  }
  long long d = 0;
  for (auto &i : aa) {
    if (i.second == 1) {
      d++;
    }
  }
  cout << d << '\n';
  for (int i = 0; i < n; i++) {
    if (aa[a[i]] == 1) {
      cout << a[i] << '\n';
      aa[a[i]] = 0;
    }
  }

  return 0;
}
