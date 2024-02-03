#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll n,k,p;
int main (int argc, char *argv[]) {
  cin>>n>>k;
  p = pow(n,k);
  cout<<p%10;
  return 0;
}
