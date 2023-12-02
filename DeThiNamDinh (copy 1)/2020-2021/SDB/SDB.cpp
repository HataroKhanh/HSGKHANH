#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  unordered_map<int, int> freq;
  for (int i = 0; i < n; i++) {
    int num;
    cin >> num;
    freq[num]++;
  }

  vector<int> uniqueNumbers;
  for (auto &p : freq) {
    if (p.second == 1) {
      uniqueNumbers.push_back(p.first);
    }
  }

  cout << uniqueNumbers.size() << "\n";
  for (int num : uniqueNumbers) {
    cout << num << "\n";
  }

  return 0;
}
