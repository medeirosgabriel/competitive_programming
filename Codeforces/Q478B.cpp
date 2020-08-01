#include <bits/stdc++.h> 
using namespace std;
#define ll long long

ll numberComb (ll n) {
    return (n * (n - 1))/2;
}

int main () {

    ll p, t;
    
    scanf("%lld %lld", &p, &t);

    // Maximum

    ll max, aux;
    aux = (p - t) + 1;
    max = numberComb(aux);

    // Minimum

    ll min, rest;
    if (p % t == 0) {
        aux = (p/t);
        min = numberComb(aux) * t;
    } else {
        rest = p % t;
        min = numberComb(p/t + 1) * rest + numberComb(p/t) * (t - rest);
    }

    cout << min << " " << max << endl;

    return 0;
}