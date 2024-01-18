#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll demi(ll n)
{
    ll d =0;
    for (ll j = 1;j*j<=n;j++)
    {
        if (n%j==0)
        {
            if (n!=j*j)
            {
                d+=1;
            }
            else d+=2;
        }
    }
    return d%2!=0;
}

int main()
{
    ll n;
    cin>>n;
    ll a[n];
    for (int i=1;i<=n;i++) cin>>a[i];

    ll dem=0;
    for (int i=1;i<=n;i++)
    {
        if (demi(a[i]))
        {
            dem++;
        }
    }
    cout<<dem;

}
