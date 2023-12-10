#include <bits/stdc++.h>
using namespace std;

bool ganhh(long long a) {
  long long ssum = 0;
  for (long long i = 1; i * i <= a; i++) {
    if (a % i == 0) {
      ssum += i;
      if (i * i != a) {
        ssum += a / i;
      }
    }
  }
  return a * 2 <= ssum;
}

int main() {
  long long n, d = 0;
  cin >> n;
  vector<long long> a;
  for (int i = 0; i < n; i++) {
    long long ip;
    cin >> ip;
    if (ganhh(ip)) {
      d++;
      a.push_back(ip);
    }
  }
  cout << d << '\n';
  for (long long &i : a) {
    cout << i << '\n';
  }
}
