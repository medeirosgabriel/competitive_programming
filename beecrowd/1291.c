#include <stdio.h>
#include <math.h>

int main() {
    
        double r;
        while(scanf("%lf", &r) != EOF) {
                double central = r*r*(1 + M_PI/3 - sqrt(3));
                double lateral = 4 * r*r*(-M_PI/6 + 1 - sqrt(3)/4);
                double rest = r * r - central - lateral;
                printf("%.3lf %.3lf %.3lf\n", central, rest, lateral);
        }
        return 0;
}

