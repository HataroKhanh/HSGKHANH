#include <bits/stdc++.h>

using namespace std;
int s(vector<int>k,int n)
{
    int d=0;
    for (int i=0;i<n;i++)
    {

        for (int j=0;j<i;j++)
        {
            k[j]=k[j]-1;
            if(k[j]<=0) return d;
        }
        d++;
    }
    return d;
}
int main() {
    int n;
    cin >> n;
    vector<int> k(n);

    for (int i = 0; i < n; i++) {
        cin >> k[i];
    }
    sort(k.rbegin(), k.rend());
    cout << s(k,n);

    return 0;
}
