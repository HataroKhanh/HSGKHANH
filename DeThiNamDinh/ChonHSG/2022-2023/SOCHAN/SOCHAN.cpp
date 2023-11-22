#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n;
  cin >> n;
  long long d = 0;
  for (long long i = 5; i <= n; i += 5) {
    if (i % 5 == 0 && i % 2 == 0) {
      d++;
    }
  }
  cout << d;
  return 0;
}
