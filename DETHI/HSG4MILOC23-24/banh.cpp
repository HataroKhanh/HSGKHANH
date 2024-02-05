#include <bits/stdc++.h>
using namespace std;
#define ll long long
int n,m,k;
int main(int argc, char const *argv[])
{
	cin>>n>>m>>k;
	if (n>k)
		cout<<n*m-n*m*0.2;
	else{
		int smin = (n*m>k*m-k*m*0.2) ? (n*m):k*m-k*m*0.2;
		cout<<smin;
	}
	return 0;
}