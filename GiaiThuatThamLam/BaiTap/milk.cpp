#include <bits/stdc++.h>
using namespace std;
bool check(pair<int,int> x,pair<int,int> y)
{
    return x.first<y.first;
}
int main() {

    int n,k;
    cin>>k>>n;
    pair<int,int> a[n];
    for (int i=0;i<n;i++) cin>>a[i].first>>a[i].second;
    sort(a,a+n,check);
    int money=0;
    for (int i=0;i<n;i++){
        if (k>a[i].second){
            k-=a[i].second;
            money+=a[i].first*a[i].second;
        }
        else if (k<=a[i].second)
        {

            money+=a[i].first*k;
            break;
        }
    }
    cout<<money; 
    

    


    return 0;
}
