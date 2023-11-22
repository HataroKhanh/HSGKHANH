#include <iostream>
#include <string>
using namespace std;
int tich(string s)
{
    int t=1;
    for(int i=0;i<s.size();i++)
    {
        t*=s[i];
    }
    return t;
}
int main() {
    string m;
    cin >> m;
    int n=stoi(m),a=0;
    for(int i=10;i<=1000000000;i++)
    {
        string t=to_string(i);
        a=1;
        for (int j=0;j<t.size();j++)
        {
            a*=t[j]-'0';
        }
        if (a==n){
            cout<<t;break;
        }
    }
    return 0;
}
