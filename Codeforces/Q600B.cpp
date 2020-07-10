#include <bits/stdc++.h> 
using namespace std;

int main() {

    int na, nb;
    scanf("%d %d", &na, &nb);
    
    int aa[na], ab[nb];

    for (int i = 0; i < na; i++) {
        scanf("%d", &aa[i]);
    }

    for (int i = 0; i < nb; i++) {
        scanf("%d", &ab[i]);
    }

    sort(aa, aa + na);

    for (int i = 0; i < nb; i++) {
        printf("%ld ", upper_bound(aa, aa + na, ab[i]) - aa); 
    }
}