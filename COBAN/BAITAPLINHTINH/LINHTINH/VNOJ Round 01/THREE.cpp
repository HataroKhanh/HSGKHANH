#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n+1];

    for (int i=1;i<=n;i++) cin>>a[i];

    int b[n+1],c[n+1];
    a[0]=b[0]=c[0]=c[n+1]=0;
    for(int i=1;i<=n;i++)
    {
        b[i]=max(b[i-1],a[i]);
    }
    for (int i=n;i>=1;i--)
    {
        c[i]=max(c[i+1],a[i]);
    }
    int smax = INT32_MAX;
    for (int i=1;i<=n;i++)
    {
        if (a[i]<b[i] and b[i]<c[i])
            smax = min(smax,a[i]+b[i]+c[i]);
    }
    cout<<smax;


}