#include <bits/stdc++.h>
using namespace std;

void lan1(int a[], int &u, int &v) {
  stack<int> ta;
  for (int i = u; i <= v; i++) {
    ta.push(a[i]);
  }
  for (int i = u; i <= v; i++) {
    a[i] = ta.top();
    ta.pop();
  }
}

int main() {
  int n, k, u, v, l, r;
  cin >> n >> k >> u >> v >> l >> r;

  int a[n + 1]; // Note: VLA, non-standard in C++
  // pair<int, int> b[k]; // Unused in this snippet

  for (int i = 1; i <= n; i++) {
    a[i] = i;
  }

  for (int i = 0; i < k; i++) {
    // int cp[n]; // Unused in this snippet
    lan1(a, u, v);
    lan1(a, l, r);
  }

  for (int i = 1; i <= n; i++) {
    cout << a[i] << '\n';
  }
  return 0;
}
