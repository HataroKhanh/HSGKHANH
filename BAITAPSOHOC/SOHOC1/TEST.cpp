#include <boost>
#include <iostream>

using namespace std;
using namespace boost::multiprecision;

int main() {
  cpp_int n;
  cin >> n;

  cpp_int factorial = 1;

  for (cpp_int i = 1; i <= n; ++i) {
    factorial *= i;
  }

  cout << factorial << endl;

  return 0;
}
