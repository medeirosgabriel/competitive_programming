#include <iostream>

using namespace std;

int main() {
 
    unsigned int i, n, fib, times, n1, n2, temp;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &fib);
        if (fib < 2) {
            cout << "Fib(" << fib << ") = " << fib << endl;
        } else {
            n1 = 0; n2 = 1;
            for (times = 2; times <= fib; times++) {
                temp = n2;
                n2 += n1;
                n1 = temp;
            }
            printf("Fib(%d) = %d\n", fib, n2);
        }
    }

    return 0;
}
