#include <bits/stdc++.h>
using namespace std;
#define N (int)10e6
vector<int> sannt() {

  vector<int> a(N, 1);
  a[0] = a[1] = 0;

  for (int i = 2; i * i < N; i++) {
    if (a[i] == 1) {
      for (int j = i * i; j <= N; j += i) {
        a[j] = 0;
      }
    }
  }
  return a;
}
int main(int argc, char *argv[]) {

  vector<int> khanh = sannt();

  cout << ((khanh[5]) ? "YES" : "NO");
  cout << ((khanh[6]) ? "YES" : "NO");
  return 0;
}
