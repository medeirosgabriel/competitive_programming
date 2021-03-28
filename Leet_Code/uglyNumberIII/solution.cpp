#include <bits/stdc++.h>
#define ll unsigned long long

using namespace std;

ll gcd (ll a, ll b) {
    return (b == 0) ? a : gcd(b, a%b);
}

ll lcm(ll a, ll b) {
    return (a * b)/gcd(a, b);
}

int nthUglyNumber(int n, int a, int b, int c) {

    ll ab = lcm(a, b);
    ll bc = lcm(b, c);
    ll ac = lcm(a, c);
    ll abc = lcm(ab, c);

    // A U B U C = A + B + C - AB - BC - AC + ABC
    // m/a = multiples less than m that are divisible by a

    ll p1 = 1, p2 = 2 * pow(10, 9), x, m;

    while (p1 < p2) {
        m = (p1 + p2)/2;
        x = m/a + m/b + m/c - m /ab - m/bc - m/ac + m/abc;
        if (x >= n) {p2 = m;}
        else {p1 = m + 1;}
    }

    return (int) p1;
}

int main() {
    cout << nthUglyNumber(3, 2, 3, 5) << endl;
    return 0;
}