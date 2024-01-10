#include <iostream>
#include <string>
#define ll long long
using namespace std;
int main()
{
    ll n,q;
    cin>>n>>q;
    ll a[n];
    a[0]=0;
    for (int i=1;i<=n;i++) {
        cin>>a[i];
        a[i]=a[i-1]+a[i];
    }

    while (q--)
    {
        ll x,y;
        cin>>x>>y;
        cout<<a[y]-a[x-1]<<'\n';
    }
    return 0;
}