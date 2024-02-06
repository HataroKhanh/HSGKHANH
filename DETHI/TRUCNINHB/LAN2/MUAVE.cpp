#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll a,b,n,k;
int main(int argc, char const *argv[])
{
	cin>>n>>k>>a>>b;
	if (k==1) a = b;
	if (n>k)
	{
		cout<<(n%k)*a+(n/k)*b;
	}
	else{
		if (b<a*n)
		{
			cout<<b;
		}
		else{
			cout<<a*n;
		}
	}
	return 0;
}