#include <bits/stdc++.h>
using namespace std;
#define ll long long
const ll smax = 1e6;
ll n,BIT[smax],a[smax],x,y;
map<int,int> compress;
void update(ll i,ll d)
{
    while (i<=n)
    {
        BIT[i]+=d;
        i+= i & (-i);
    }
}

ll query(ll i)
{
    ll ssum = 0;
    while (i>0)
    {
        ssum += BIT[i];
        i -= i & (-i);
    }       
    return ssum;
}
int main(int argc, char const *argv[])
{
    cin>>n;
    for (ll i=1;i<=n;i++){
        cin>>x>>y;
        compress[i] = x;
        update(i,y);
    }

    for (auto i:compress)
        cout<<i.first<<i.second<<' ';

}