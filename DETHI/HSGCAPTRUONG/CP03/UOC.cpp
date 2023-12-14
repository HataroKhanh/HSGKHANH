#include <bits/stdc++.h>
#include <ios>
using namespace std;

void uoc(long long &a, vector<long long> &B) {
  for (long long i = 1; i * i <= a; i++) {
    if (a % i == 0) {
      B.push_back(i);
      if (a != i * i) {
        B.push_back(a / i);
      }
    }
  }
  sort(B.begin(), B.end());
}
int main() {

  long long a;
  cin >> a;
  vector<long long> B;
  uoc(a, B);

  for (long long &i : B) {
    cout << i << '\n';
  }

  return 0;
}
