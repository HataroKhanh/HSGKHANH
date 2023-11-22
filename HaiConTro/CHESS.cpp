#include <bits/stdc++.h>
#include <cstdio>
#include <functional>
#include <vector>
#define N 1003
using namespace  std;
int main(){
    int n,s=0;
    cin>>n;
    vector<int> a(n);
    vector<int> b(n);
    for (int i=0;i<n;i++) {
        cin>>a[i];
        cin>>b[i];
    }
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    int i=0,j=0;
    while (j<n)
    {
        if (b[j]>a[i])
        {
            s+=2;
            i++;j++;
        }
        else if (b[j]==a[i])
        {
            s+=1;
          i++;j++;
        }
        else{
            j++;
        }
    }
    cout<<s;

  return 0;
}  
