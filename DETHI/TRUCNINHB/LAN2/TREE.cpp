#include <bits/stdc++.h>
using namespace std;
#define ll long long
const ll SMAX = 10e4;
ll n,a[SMAX],b[SMAX];
ll i=0,j=1;
ll dmax = -1;
bool nt(ll n){
	if (n<=1) return false;
	else{
		for (ll i=2;i*i<=n;i++)
		{
			if (n%i==0) return false;
		}
	}
	return true;
}
int main()
{
	cin>>n;
	for ( ll i=1;i<=n;i++) cin>>a[i];
	for ( ll i=1;i<=n;i++) b[i] = a[i] +b[i-1];
	
	for (ll i=1;i<=n;i++)
	{
		for (ll j=i;j<=n;j++)
		{
			if (nt(b[j]-b[i-1]))
			{
				dmax = max(dmax,j-i+1);
			}
		}
	}	
	cout<<dmax;
	return 0;
}