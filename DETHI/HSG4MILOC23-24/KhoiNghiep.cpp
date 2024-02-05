#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define myPair pair<ll, ll>
const ll MAX = 10e5 + 3;

myPair k[MAX];
bool comparePairs(const myPair &a, const myPair &b)
{
    return a.second < b.second;
}

int main(int argc, char const *argv[])
{
    ll n, sum = 0;
    cin >> n;

    for (ll i = 1; i <= n; i++)
    {
        cin >> k[i].first >> k[i].second;
    }

    ll l = 0, r = 0;

    



    
    return 0;
}
