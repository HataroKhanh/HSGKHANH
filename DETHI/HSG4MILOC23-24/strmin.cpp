#include <bits/stdc++.h>
#include <vector>
#include <string>

using namespace std;

#define ll long long
int x,y,z,n;
int main(int argc, char const *argv[])
{
	cin>>n>>x>>y>>z;
	string t;
	for (int i=48;z!=0;i++)
	{
		t+=char(i);
		z--;
	}
	for (int i=65;y!=0;i++)
	{
		t+=char(i);
		y--;
	}
	for (int i=97;x!=0;i++)
	{
		t+=char(i);
		x--;
	}
	cout<<t;
	return 0;
}