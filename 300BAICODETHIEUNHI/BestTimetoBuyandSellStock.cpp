#include <bits/stdc++.h>
#include <climits>
using namespace std;

class Solution {
public:
  int maxProfit(vector<int> &prices) {
    int n = prices.size();
    vector<int> minPrices(n), maxPrices(n);

    // Initialize the first element of minPrices with the first price.
    minPrices[0] = prices[0];
    // Populate minPrices with the minimum price seen so far from the start.
    for (int i = 1; i < n; i++) {
      minPrices[i] = min(minPrices[i - 1], prices[i]);
    }

    // Initialize the last element of maxPrices with the last price.
    maxPrices[n - 1] = prices[n - 1];
    // Populate maxPrices with the maximum price seen so far from the end.
    for (int i = n - 2; i >= 0; i--) {
      maxPrices[i] = max(maxPrices[i + 1], prices[i]);
    }

    int maxProfit = 0;
    // Calculate the maximum profit.
    for (int i = 0; i < n; i++) {
      maxProfit = max(maxProfit, maxPrices[i] - minPrices[i]);
    }
    return maxProfit;
  }
};

int main() {
  Solution solution;
  vector<int> prices = {7, 1, 5, 3, 6, 4};
  cout << solution.maxProfit(prices);
  return 0;
}
