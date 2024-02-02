#include <algorithm>
#include <bits/stdc++.h>
#include <string>
#include <vector>
using namespace std;
#define ll long long
const ll SMAX = 105;
ll n,dmax;
string a[SMAX];

ll dcout(string &i)
{
  ll sdem = 0; 
  for (char j:i){
    if ('0'<=j and j<='9')
    {
      sdem+=j-'0';
    }
  }
  return sdem/i.size();
}
int main(int argc, char *argv[]) {
  cin >> n;
  for (ll i=1;i<=n;i++)
  {
    cin>>a[i];
  }

 for (ll i=1;i<=n;i++)
 {
   dmax = max(dmax,dcout(a[i]));
 }
 for (ll i =1;i<=n;i++)
 {
   if (dcout(a[i])==dmax){
     cout<<a[i];
     break;
   }
 }


  return 0;
}
