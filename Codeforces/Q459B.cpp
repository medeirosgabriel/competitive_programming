#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main () {

    ll n;

    scanf("%lld", &n);

    ll f, max = -1, min = 1000000000, contMax, contMin;

    for (ll i = 0; i < n; i++) {
        scanf("%lld", &f);

        if (f > max) {
            max = f;
            contMax = 1;
        } else if  (f == max) {
            contMax ++;
        }

        if (f < min) {
            min = f;
            contMin = 1;
        } else if  (f == min) {
            contMin ++;
        }
    }

    ll p;

    if (min == max) {
        p = ((contMax) * (contMax - 1))/2;
    } else {
        p = contMax * contMin;
    }
   
    cout << max - min << " " << p << endl;

    return 0;
}