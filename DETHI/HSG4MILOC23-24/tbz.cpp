#include <bits/stdc++.h>
#include <vector>
#include <string>
using namespace std;
#define ll long long
const ll SMAX = 10e7+3;
ll n,a[SMAX],sum[SMAX];
#include <unordered_map>
unordered_map<ll,ll> k;
ll i=1,j=1;
int main(int argc, char const *argv[])
{
	cin>>n;
	for (ll i=1;i<=n;i++)
		cin>>a[i];

	for (ll i=1;i<=n;i++)
		sum[i]=a[i]+sum[i-1];
	ll dem = 0;
	for (ll i=1;i<=n;i++)
	{
		k[sum[i]]++;
	}
	for (pair<ll,ll> i:k)
	{
		dem+=i.second;
	}
	cout<<dem/2;
	return 0;
}