#include <bits/stdc++.h>
using namespace std;

int main(){

    int n, t, c, current = 0, cont = 0, aux = 0;

    scanf("%d %d %d", &n, &t, &c);

    for (int i = 0; i < n; i++) {
        scanf("%d", &current);
        if (current <= t) {
            aux++;
        }else {
            cont += (aux >= c) ? aux - c + 1 : 0;
            aux = 0;
        }
    }

    cont += (aux >= c) ? aux - c + 1 : 0;

    cout << cont << endl;

	return 0;
}