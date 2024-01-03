#include <algorithm>
#include <bits/stdc++.h>
#define ll long long
using namespace std;
bool khanh(ll d,vector<ll> a,ll n)
{
  ll k=1,i=0;
  while (i<n)
  {
    if (a[i]>=k)
    {
      i+=d-1;
      k++;
    }
    else{
      return false;
    }
  }
  return true;
  
}
int main (int argc, char *argv[]) {
  ll n,smax=INT_MIN;
  cin>>n;
  vector<ll> a(n),b(n);
  for (int i=0;i<n;i++) 
  {cin>>a[i];
    smax=max(smax,a[i]);}
  
  sort(a.begin(),a.end());
  ll left=0,right=smax,mid;

  while (left < right) {
    mid = left + (right - left) / 2;

    if (khanh(mid, a, n)) {
        right = mid;
    } else {
        left = mid + 1;
    }
  }
  cout << left;


  return 0;
}
