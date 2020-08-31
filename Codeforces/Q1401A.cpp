#include <bits/stdc++.h>

using namespace std;

int main(){
	int n,a,k;
	scanf("%d",&n);
	while(n--){
		scanf("%d %d",&a,&k);
		if (a <= k) {
            cout << k - a << endl;
        } else {
			((a - k) % 2) ? cout << 1 << endl : cout << 0 << endl;
		}
	}
	return 0;
}
