#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll n,ip,le=0,chan=0;
ll uoc(ll ip)
{
	ll d = 0;
	for ( ll i=1;i*i<=n;i++)
	{
		if (n%i==0)
		{
			d++;
			if (i*i!=n)
			{
				d++;
			}
		}
	}
	return d;

}
int main(int argc, char const *argv[])
{
	cin>>n;
	while (n--)
	{
		cin>>ip;
		ll kq = uoc(ip);
		if (kq%2==0) chan++;
		else le++;
	}
	cout<<chan<<'\n'<<le;
	return 0;
}
