#include <bits/stdc++.h>

using namespace std;
bool check(pair<int,int> a,pair<int,int> b)
{
    return a.first<=b.first || a.second<=b.second;
}
int main()
{
    int n,m;
    cin>>n>>m;
    pair<int,int> a[n];

    for (int i=0;i<n;i++)
    {
        cin>>a[i].first>>a[i].second;
    }

    bool phieu=true;
    sort(a,a+n,check);
    for (int i=0;i<n;i++) cout<<a[i].first<<" "<<a[i].second<<"\n";
    cout<<'\n';
    int d=0;
    for (int i=0;i<n;i++)
    {
        if (a[i].first+a[i].second<=m)
        {
            m-=a[i].first+a[i].second;
            if (m>=0) d++;
        }
        else if ((a[i].first+a[i].second>m && phieu==true))
        {
            m-=a[i].first/2+a[i].second;
            phieu=false;
            if (m>=0) d++;
        }
        else break;
    }
    cout<<d;
    return 0;
}
