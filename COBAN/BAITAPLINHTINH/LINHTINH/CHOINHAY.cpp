#include <bits/stdc++.h>
using namespace std;

int step(int &a, int &b, int &c) {
    int l, r, dem = 0;
    while (!(a == b || b == c)) {
        l = b - a;
        r = c - b;
        if (r > l) {
            a = c - 1;
            dem++;
            swap(a, b);
        } else {
            c = a + 1;
            dem++;
            swap(c, b);
        }
    }
    return dem;
}

int main() {
    int a, b, c;
    while (cin >> a >> b >> c) {
        cout << step(a, b, c) - 1<< endl;
    }
    return 0;
}
