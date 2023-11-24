#include <fstream>
#include <iostream>
#include <string>
using namespace std;

string s[1001];

void tt(int x) {
  int du = 0;
  for (int i = s[x - 1].length() - 1; i >= 0; i--) {
    int f = (s[x - 1][i] - '0') * 2;
    s[x] = char((f + du) % 10 + '0') + s[x];
    du = (f + du) / 10;
  }
  if (du > 0) {
    s[x] = char(du + '0') + s[x];
  }
  if (x % 2 == 1) {
    int i = s[x].length() - 1;
    do {
      int f = (s[x][i] - '0') - 9;
      s[x][i] = char(f % 10 + '0');
      du = 1 - f / 10;
    } while (du != 0);
  } else {
    s[x][s[x].length() - 1] = char(s[x][s[x].length() - 1] + 1);
  }
}

int main() {
  ifstream fi("tile.inp");
  ofstream fo("tile.out");
  s[0] = "0";
  s[1] = "1";
  int c = 1;
  int n;
  while (fi >> n) {
    while (c < n) {
      c++;
      tt(c);
    }
    fo << s[n] << endl;
  }
  fi.close();
  fo.close();
  return 0;
}
