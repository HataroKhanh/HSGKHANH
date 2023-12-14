#include <iostream>

#include <vector>
using namespace std;
int main() {

  const int N = 1000000;
  vector<bool> isPrime(N + 1, true);
  isPrime[0] = isPrime[1] = false;
  for (int i = 2; i * i <= N; i++) {
    if (isPrime[i]) {
      for (int j = i * i; j <= N; j += i) {
        isPrime[j] = false;
      }
    }
  }
  int n;
  cin >> n;

  pair<int, int> a[n + 1];

  for (int i = 0; i < n; i++) {
    cin >> a[i].first >> a[i].second;
  }

  for (int i = 0; i < n; i++) {
    int d = 0;
    for (int j = a[i].first; j <= a[i].second; j++) {
      if (isPrime[j]) {
        d++;
      }
    }
    cout << d << '\n';
  }
  return 0;
}
