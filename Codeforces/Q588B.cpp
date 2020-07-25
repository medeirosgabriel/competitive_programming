#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {

    ll n;

    scanf("%lld", &n);

    for (ll i = 2; i <= sqrt(n); i++) {
        while(n % (i*i) == 0) {
            n /= i;
        }
    }

    cout << n << endl;

    return 0;
}