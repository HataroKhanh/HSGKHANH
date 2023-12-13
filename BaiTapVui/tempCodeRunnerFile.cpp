
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
  int t,i=0,j=n-1;
  while (i<n && j<n)
  {
    t=a[i]+b[j];
    
    if (t<0)
    {
      i++;
    }
    else if (t>0)
    {
      j--;
    }
    else break;
    if (i==n-1)
    {
      for (int j;j>=0;j--)
      {
        t=a[i]+b[j];
        if (t<=0){break;}
      }
    }
    else if (j==0)
      {
        for (int i;i<n;i++)
        {
          t=a[i]+b[j];
          if (t>=0){break;}
        }
      }
  }
  cout<<abs(t);
  return 0;
}