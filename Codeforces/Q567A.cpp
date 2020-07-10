#include <bits/stdc++.h> 
using namespace std;

int main() {

    int n, i, s, b;
    scanf("%d", &n);
    int a[n];
    
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    for (i = 0; i < n; i++) {
        if (i != 0 && i != n - 1) {
            s = abs(a[i - 1] - a[i]) < abs(a[i] - a[i + 1]) ? 
                a[i - 1] - a[i] : a[i] - a[i + 1];
            b = abs(a[0] - a[i]) > abs(a[i] - a[n - 1]) ? 
                abs(a[0] - a[i]) : a[i] - a[n - 1];
        }else if (i == 0) {
            s = a[0] - a[1];
            b = a[n -1] - a[0];
        }else {
            s = a[i] - a[i - 1];
            b = a[i] - a[0];
           
        }
        printf("%d %d\n", abs(s), abs(b));
    }

    cout << endl;
}