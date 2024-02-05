#include <bits/stdc++.h>
using namespace std;
#define ll long long
const ll MAX = 10e5 + 3;

ll n, kq, a[MAX], sum = 0;
map<ll,ll> k;
int main() {
    cin >> n >> kq;

    for (ll i = 1; i <= n; i++) {
        cin >> a[i];
        k[a[i]]++;
    }

    for (ll i = 1; i <= n; i++) {
    	if (k[a[i]+kq]!=0)
        	sum+=k[a[i]]*k[a[i]+kq];
    }

    cout << sum/2;

    return 0;
}
