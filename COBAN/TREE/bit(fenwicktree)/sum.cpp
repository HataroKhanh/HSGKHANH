#include <bits/stdc++.h>
#define ll long long
using namespace std;
const ll NMAX = 1e6;

ll a[NMAX], n, p;
ll T[NMAX]; // Cây BIT

ll getPrefixSum(int x) {
    // Tính tổng a[1] + ... + a[x]
    ll res = 0;
    while (x > 0) {
        res += T[x];
        x = x - (x & (-x)); // Lùi về giá trị cung cấp không chung tổ tiên và con
    }
    return res;
}

void updateBIT(int x, int p) {
    // Tăng nút x và tổ tiên của x lên p đơn vị
    while (x <= n) {
        T[x] += p;
        x += (x & (-x));
    }
}

int main() {
    cin >> n >> p;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        updateBIT(i, a[i]); // Vì ban đầu cây BIT == 0
    }



    while (p--) {
        int ip;
        cin >> ip;
        if (ip == 1) {
            int x, p;
            cin >> x >> p;
            updateBIT(x, p);
        } else if (ip == 2) {
            int x;
            cin >> x;
            cout << getPrefixSum(x) << '\n';
        } else {
            int x, y;
            cin >> x >> y;
            cout << getPrefixSum(x) - getPrefixSum(y-1) << '\n';
        }
            for (int i=1;i<=n;i++)
    {
        cout<<T[i]<<' ';
    }
    cout<<endl;
    }
    return 0;
}
