#include <bits/stdc++.h>
#include <cstdio>
using namespace  std;

int main(){
    int n,s,k=0,d=1000002;
    cin>>n>>s;
    vector<int> a(n,0);

    //for (int i=0;i<n;i++) cin>>a[i];
    
    
    int i=0,j=0;
    while (j>=i && j<n)
    {
        if (k<s){
            k+=a[j];
            j++;
        }
        else if (k>s){
            k-=a[i];
            i++;
        }
        else {
            d=min(d,j-i);
            cout<<i<<" "<<j<<'\n';
            j++;
        }
        
    }
    cout<<d;
  return 0;
}  
