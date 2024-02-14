#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll a,b,c,sum = 1;
int main(int argc, char const *argv[])
{
	cin>>a>>b>>c;
	cout<<max(a,max(b,c))<<'\n';
	cout<<gcd(a,gcd(b,c))<<'\n';
	for(ll i=0;i<=10;i++)
		for (ll j=0;j<=10;j++)
			for (ll k = 0;k<=10;k++)
				if (a*pow(10,i)+b*pow(10,j)==c*pow(10,k)){
					cout<<i<<' '<<j<<' '<<k;
					return 0;
				}
	cout<<-1;
	return 0;
}
