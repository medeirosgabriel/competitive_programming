#include <bits/stdc++.h>
using namespace std;

int main() {

    map<string, int> words;
    int n;
    char key[32];

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%s", &key);
        if (words[key]) {
            printf("%s%d\n", key, words[key]);
            words[key] ++;
        }else {
            printf("OK\n");
            words[key] ++;
        }
    }

	return 0;
}