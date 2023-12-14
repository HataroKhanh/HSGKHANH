#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;cin>>n;
  int a[n],b[n];
  for (int i = 0; i < n; i++) {
    cin>>a[i];
  }
  for (int i = 0; i < n; i++) {
    cin>>b[i];
  }

  sort(a,a+n);
  sort(b,b+n);
  int smin=10000000;
  int t,i=0,j=n-1;
  while (i<n && j>=0)
  {
    t=a[i]+b[j];
    smin=min(smin,abs(t));
    if (t<0){
      i++;
    }
    else if (t>0) j--;
    else {cout<<0;break;}
  }
  cout<<smin;
}