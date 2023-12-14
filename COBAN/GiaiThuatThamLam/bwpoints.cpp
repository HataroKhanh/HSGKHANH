#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n+3],b[n+3];

    for (int i=0;i<n;i++) cin>>a[i];
    for (int i=0;i<n;i++) cin>>b[i];

    sort(b,b+n);

    int i=0,j=0;
    int d=0;
    while (i<n && j<n)
    {
        if (a[i]+b[i]){}
    }

    return 0;
}