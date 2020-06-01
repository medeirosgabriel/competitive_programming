#include <bits/stdc++.h>

using namespace std;

int main () {

    int n, k, cn;
    int v[100] = {0};

    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &cn);
        v[cn%k] ++;
    }

    int cont = v[0]/2;

    for (int i = 1; i < k/2; i++) {
        cont += min(v[i], v[k - i]);
    }

    if (k%2==0) {
        cont += v[k/2]/2;
    } else {
		cont += min(v[k/2], v[k - k/2]); 
	}

	printf("%d\n", cont*2);

    return 0;
}