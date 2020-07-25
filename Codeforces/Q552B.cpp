#include <bits/stdc++.h> 
#define ll long long

using namespace std;

int main() {

    ll n;
    scanf("%lld", &n);

    ll nd = 0;
    ll aux = n;
    
    while (aux != 0) {
        aux /= 10;
        nd ++;
    }

    ll res = 0, cont = 9, mult = 1, dig = 1;

    while (n - cont >= 0) {
        res += 9 * mult * dig;
        dig ++; 
        mult *= 10;
        cont += 9 * mult; 
    }

    res += (n - (cont - 9 * mult)) * nd;

    cout << res << endl;

    return 0;
}