#include <bits/stdc++.h>

using namespace std;

bool check(pair<int,int> a,pair<int,int> b){
    return  a.first>=b.first && a.second <= b.second; 
}
int main()
{
//freopen("coins.inp","r",stdin);
//freopen("coins.out","w",stdout);
    int n,m;
    cin>>n>>m;

    pair<int,int> a[n];
    
    for (int i=0;i<n;i++)
    {
        cin>>a[i].first;
    }
    for (int i=0;i<n;i++)
    {
        cin>>a[i].second;
    }
    
    sort(a,a+n,check);
   // for (int i=0;i<n;i++) cout<<a[i].first<<" "<<a[i].second<<'\n';
    for (int i=0;i<n;i++)
    {
        if (m+a[i].first>=a[i].second)
        {
            m+=a[i].first;
        }
        else break;
    }
    cout<<m;
    return 0;
}
