#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a[5];
    for (int i = 0; i < 5; i++)
    {
        cin >> a[i];
    }
    sort(a, a + 5);
    int smax = 0;
    for (int i = 0; i < 5; i++)
    {
        smax += a[i];
    }

    cout << "Tong Lon Nhat: " << smax - a[0] << " Tong nho nhat: " << smax - a[4];

    return 0;
}
