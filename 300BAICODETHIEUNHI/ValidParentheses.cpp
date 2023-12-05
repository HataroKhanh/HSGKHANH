#include <algorithm>
#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool khanh(string a) {
  stack<char> aa;

  for (char i : a) {
    if (i != '"') {
      aa.push(i);
    } if (!aa.empty()) {
      if ((i == '}' && aa.top() == '{') || (i == ']' && aa.top() == '[') ||
          (i == ')' && aa.top() == '(') || (i == '>' && aa.top() == '<')) {
        aa.pop();
      }
    }
  }
  return aa.empty();
}

int main() {
  string s;
  cin >> s;
  cout << (khanh(s) ? "true" : "false");
}
