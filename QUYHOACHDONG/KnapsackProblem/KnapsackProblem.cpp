#include <iostream>
using namespace std;
#define N 1000001
int a[N], solu[N];

int main(int argc, char *argv[]) {
  int n,k;
  cin >> n >> k;

  for (int i = 1; i <= n; i++) {
    cin >> a[i];
  }

  solu[0] = 0, solu[1] = a[1];
  for (int i = 2; i <= n; i++) {
    solu[i] = min(solu[i - 2], solu[i - 1] + a[i]);
  }
  cout << solu[n];
  return 0;
}
