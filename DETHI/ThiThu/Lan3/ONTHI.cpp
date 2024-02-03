#include <bits/stdc++.h>
using namespace std;
#define ll long long
const ll SMAX = 10e6;
ll n,c,k;
pair<ll,ll> a[SMAX];
bool check (pair<ll,ll> a,pair<ll,ll> b)
{
    return a.second>b.second || a.first > b.first;
}
int main(int argc, char const *argv[])
{
    cin>>n>>c>>k;
    for (ll i=1;i<=n;i++) cin>>a[i].first>>a[i].second;

    sort(a+1,a+n+1,check);
    ll ssum = 0;
    for (ll i=1;i<=n;i++)
    {
    
    }
    return 0;
}

