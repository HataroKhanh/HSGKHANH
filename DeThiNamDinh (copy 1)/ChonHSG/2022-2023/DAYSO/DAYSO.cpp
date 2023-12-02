#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> a(n),
      b(n + 1); // Use vectors and add an extra space for b[0] = 0.
  vector<pair<int, int>> aa;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    b[i + 1] = b[i] + a[i]; // Compute prefix sums with proper indices.
  }

  int i = 0, j = 0, d = 0;
  while (j < n) {
    // Check average with floating point division.
    while (i < j && (b[j + 1] - b[i]) / static_cast<double>(j - i + 1) < k) {
      i++;
    }
    d = max(d, j - i + 1);        // Correctly calculate the length.
    aa.push_back({i + 1, j + 1}); // Store 1-based index pairs.
    j++;
  }
  cout << d << '\n';

  // Iterate through the vector and output the pairs that have the length d.
  for (const auto &p : aa) {
    if (p.second - p.first == d) {
      cout << p.first << " " << p.second << "\n";
    }
  }
  return 0;
}
