#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {

    int n;
    scanf("%d", &n);
    ll da[2000] = {0}, db[2000] = {0};
    int x, y;
    
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &x, &y);
        da[x + y]++;
        db[1000 + x - y]++;
    }

    ll result = 0;

    for (int i = 0; i < 2000; i++) {
        result += (da[i] * (da[i] - 1))/2;
        result += (db[i] * (db[i] - 1))/2;
    }

    cout << result << endl;

    return 0;
}