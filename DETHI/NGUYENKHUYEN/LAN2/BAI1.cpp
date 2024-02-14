#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll a,b,c,sum = 1;
int main(int argc, char const *argv[])
{
	cin>>a>>b>>c;
	for (ll i=a;i<=b;i++)
	{
		sum*=i;
	}
	cout<<sum%c;
	return 0;
}
