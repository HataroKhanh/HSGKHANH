#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int k[n];
    for (int i=0;i<n;i++)
    {
        cin>>k[i];
    }
    int smax=0,dmax=-10e6,i=0,j=0;
    while (i<=j && j<n)
    {   
        smax += k[j];
        dmax=max(dmax,smax);
        if (smax<0) smax=0;
        j++;

    }
    cout<<dmax;
    return 0;
}
