#include <iostream>
#include <vector>
using namespace std;
int main() {
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  int j = 0, i = 0, sum = 0;
  while (j < n) {
    sum += a[j];
    while (sum > k && i < j) {
      sum -= a[i];
      i++;
    }
    if (sum == k) {
      for (int d = i; d <= j; d++) {
        cout << a[d] << " ";
      }
      cout << endl;
    }
    j++;
  }
  return 0;
}
