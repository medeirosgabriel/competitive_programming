#include <bits/stdc++.h>
#define ll unsigned long long

using namespace std;

int main() {

    int n;
    scanf("%d", &n);
    ll array[n];

    for (int i = 0; i < n; i++) {
        scanf("%lld", &array[i]);
    }

    for (int i = 0; i < n; i++) {

        while (array[i] % 2 == 0) {
            array[i] = array[i]/2;
        }

        while (array[i] % 3 == 0) {
            array[i] = array[i]/3;
        }
    }

    bool r = 1;
    int i = 0;

    while (r && i < n - 1) {
        r = (array[i] == array[i + 1]);
        i++;
    }

    if (r) {
        cout << "Yes" << endl; 
    }else {
        cout << "No" << endl;
    }
}