#include <bits/stdc++.h>
#include <cstdio>
using namespace  std;

int giaithua(const int &n)
{
  int s=1;
  for (int i=1;i<=n;i++)
  {
    s*=i;
  }
  return s;
}
int tohop(const int &n)
{
  return giaithua(n)/(giaithua(n-3)*giaithua(3));
}
int main (int argc, char *argv[]) {
  int n,k;
  cin>>n>>k;
  vector<int> a(n);
  for(int i=0;i<n;i++)
  {
    cin>>a[i];
  }
  sort(a.begin(),a.end());
  int i=0,j=2,s=0,sdem=0;
  for (int i:a) cout<<i<<" ";
  cout<<'\n';
  for(int j=2;j<n;j++)
  {
    if (a[j]-a[i]<=3)
    {
      sdem+=tohop(j-i+1);
      //cout<<a[i]<<" "<<a[j]<<'\n';
    }
    else {
      i++;
      j--;
    }
    //cout<<j<<"\n";
    if (j==n-1)
    {
      for (int k=i;k<=j-2;k++)
      {
        if (a[j]-a[k]<=3) {sdem+=tohop(j-k+1);}
      }
    }
  }
  cout<<sdem;
  return 0;
}  
