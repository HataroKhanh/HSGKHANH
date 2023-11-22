#include <bits/stdc++.h>
#include <ios>
using namespace  std;
#include <iostream>
int caua(vector<int> a,int n,int s)
{
  while (a.size()>n)
  {
    a.erase(a.begin()+s);
  }
  return a[s]; 
6
}
int caub(vector<int> a,int n,int s)
{
     
}
int main()
{
  int n,s;
  cin>>n>>s;  
  vector<int> a;
  for (int i=0;i<n;i++) a.push_back(i+1); 
  cout<<caua(a,  n,  s);
  return 0;
}
