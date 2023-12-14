#include <iostream>
using namespace std;
int main() {
  float ax, ay, bx, by, cx, cy;
  cin >> ax >> ay >> bx >> by >> cx >> cy;

  cout << ((ax / ay == bx / by && bx / by == cx / cy && ax / ay == cx / cy)
               ? "YES"
               : "NO");
  return 0;
}
