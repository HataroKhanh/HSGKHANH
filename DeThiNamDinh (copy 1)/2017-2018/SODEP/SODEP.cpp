#include <bits/stdc++.h>
using namespace std;
bool sodep(int a) {
  int k = 0;
  for (int i = 1; i <= a; i++) {
    if (a % i == 0) {
      k++;
    }
  }
  return a % k == 0;
}
int main(int argc, char *argv[]) {

  int a;
  cin >> a;
  if (sodep(a))
    cout << "CO";
  else
    cout << "KHONG";
  return 0;
}
