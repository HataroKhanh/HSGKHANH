#include <bits/stdc++.h>
#include <string>
using namespace std;

bool check(string s,string ip)
{
    short time = 2;
    if (s.size()!=ip.size())
    {
        return false;
    }

    for (int i=0;i<s.size();i++)
    {
        if (s[i]!=ip[i])
        {
            if (time!=0) time--;
            else{
                return false;
            }
        }
    }
    return true;
}
int main(int argc, char const *argv[])
{
    string s,ip;
    int n,i=1;
    cin>>s>>n;
    bool is = false;
    while(n--)
    {
        cin>>ip;
        if (check(s,ip))
        {
            cout<<i<<'\n';
            is = true;
        }
        i++;
    }
    if (is==false)
    {
        cout<<0;
    }
    return 0;
}
