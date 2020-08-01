#include <bits/stdc++.h>
using namespace std;

int main() {

    long long cont = 0;
    int n, v, l = 0, a = 0;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &v);
        if (v == 1) {
            a++;
            cont = (cont == 0) ? 1 : cont;
            cont *= (a == 1) ? 1 : i - l;
            l = i;
        }
    }

    cout << cont << endl;

    return 0;
}