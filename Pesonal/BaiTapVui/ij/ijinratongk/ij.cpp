#include <bits/stdc++.h>
using namespace  std ;
int main (int argc, char *argv[]) {
  
  int n,k;
  cin>>n>>k;
  int a[n];
  
  for (int i=0;i<n;i++)
  {
    cin>>a[i];
  }

  int s=0,dem=0;
  map<int,int> aa;
  int j=0;
  for (int i=0;i<n;i++)
  {
    s+=a[i];
    if (aa[s-k]){
      for (int m=(s-k);m<i;m++)
      {
        cout<<a[m];
      }
      cout<<'\n';
    }
    dem+=aa[s-k];
    aa[s]+=1;
  }
  return 0;
}
