#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n), b(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    b[0] = a[0];
    for (int i = 1; i < n; i++) {
        b[i] = b[i - 1] + a[i];
    }

    int smin = INT_MAX;
    for (int i = 0; i < n; i++) {
        if (b[i] >= k) {
            int al = i + 1;
            smin = min(smin, al);
        }
        auto it = lower_bound(b.begin() + i + 1, b.end(), k + b[i]);
        if (it != b.end()) {
            int al = it - b.begin() - i;
            smin = min(smin, al);
        }
    }
    if (smin == INT_MAX) {
        cout << "No valid subarray found" << endl;
    } else {
        cout  <<" "<<smin << endl;
    }

    return 0;
}
