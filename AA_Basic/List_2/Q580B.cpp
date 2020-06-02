#include <bits/stdc++.h>
#define MAX 1000000
#define ll unsigned long long

using namespace std;

int upperBound(pair<int, ll> a[MAX], int n, int w);

int main() {

    int n;
    ll d;

    scanf("%d %lld", &n, &d);

    pair<int, ll> a[n];

    for (int i = 0; i < n; i++) {
        scanf("%d %lld", &a[i].first, &a[i].second);
    }

    sort(a, a + n);

    for (int i = 0; i < n; i++) {
        a[i].second += (i != 0) ? a[i - 1].second : 0;
    }

	int r;
    ll v, max = 0;
	for (int i = 0; i < n; i++) {
		r = upperBound(a, n, a[i].first + d - 1);
		r = (r == -1) ? n - 1 : r - 1;
        v = (i != 0) ? a[r].second - a[i - 1].second : a[r].second;
		if (v  > max) {
			max = v;
		}
	}

	cout << max << endl;
}

int upperBound(pair<int, ll> a[MAX], int n, int w) {
    int l = 0, r = n - 1, m;
    while (l <= r) { 
		m = (l + r)/2;
		if (w < a[m].first) {
			r = m - 1;
		}else {
			l = m + 1;
		}
    }
	return (l > n -1) ? -1 : l;
}