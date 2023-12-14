#include <bits/stdc++.h>
#include <functional>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n];
    for (int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    
    sort(a,a+n,greater<int>());
    int m=0;
    for (int i=2;i<n;i+=3)
    {
        m+=a[i];
    }
    cout<<m;


    return 0;
}
