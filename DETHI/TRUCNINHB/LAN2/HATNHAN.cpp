#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll n,k;
vector<ll> uoc(string s){
	vector<ll> k;
	for (ll i=1;i*i<=s.size();i++)
	{
		if (n%i==0)  k.push_back(i) ;
	}  
	return k; 
}  
string schar(string s,ll n,ll sc){
	string text,k;
	for (ll i=0;i<sc;i++)
	{
		k+=s[i];
	}
	for (ll i=0;i<n;i++)
	{
		text+=k;
	}
	return text;
}
string hatnhan(vector<ll> k , string &s ){
	for (ll i : k)
	{
		string t = schar(s,s.size())
	}
} 
int main(int argc, char const *argv[])
{

	cin>>n;
	while (n--)
	{

	}
	return 0;
}