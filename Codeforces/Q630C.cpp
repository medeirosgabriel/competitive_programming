#include <bits/stdc++.h>

using namespace std;

int main(){

    int n;
    scanf("%d", &n);

    long long r = 0;

    for (int i = 1; i <= n; i++) {
        r += pow(2, i);
    }

    cout << r << endl;

    return 0;
}