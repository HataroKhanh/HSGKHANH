
#include <bits/stdc++.h>
#include <cstdio>
using namespace  std; 
bool khanh(const string &a,const string &b)
{
  return a+b>b+a;
}
int main (int argc, char *argv[]) {
  string s;
  vector<string> a;
  freopen("NUMCON.INP", "r", stdin);
  freopen("NUMCON.OUT", "w", stdout);

  while (cin>>s)
  {
    a.push_back(s);
  }
  sort(a.begin(),a.end(),khanh);
  for (int i=0;i<a.size();i++)
  {
    cout<<a[i];
  }
  return 0;
}  
