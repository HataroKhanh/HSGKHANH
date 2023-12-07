#include <bits/stdc++.h>
using namespace std;
void uoc(int &a) {
  for (int i = 1; i <= a; i++) {
    if (a % i == 0) {
      cout << i << "\n";
    }
  }
}
int main() {

  int a;
  cin >> a;
  uoc(a);

  return 0;
}
