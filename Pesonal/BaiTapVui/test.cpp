#include <iostream>
using namespace std;

#pragma GCC target ("avx2")
#pragma GCC optimization ("O3")
#pragma GCC optimization ("unroll-loops")

int cnt = 0;

int main() {
    for (int i = 1; i <= 30000; i++) {
        for (int j = 1; j <= 30000; j++) {
            if ((i % j) <= 10) cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
}
