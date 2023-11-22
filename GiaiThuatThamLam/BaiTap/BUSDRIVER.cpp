#include <bits/stdc++.h>
using namespace std;
#define ll 100000000;
int a[101];
int b[101];



int tientra(int &n,int &d,int &r)
{
    int tien=0;
    for (int i=0;i<n;i++)
    {
        if (a[i]+b[i]>d)
        {
            tien+=((a[i]+b[i])-d)*r;          
        }
    }
    return tien;
} 
void kiemtra(int &n,int &d,int &r)
{
    for (int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for (int i=0;i<n;i++)
    {
        cin>>b[i];
    }
    sort(a,a+n);
    sort(b,b+n,greater<int>());
}
int main()
{
    int n,d,r;
    cin.tie(0);
    while (true)
    {
        cin>>n>>d>>r;
        if (n==0 && d==0 && r==0) break;
        kiemtra(n,d,r);
        cout<<tientra(n,d,r)<<'\n';
    }
    return 0;
}