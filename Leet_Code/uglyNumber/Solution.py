class Solution {
    public int nthUglyNumber(int n) {
        int[] results = new int[n];
        for (int i = 0; i < n; i++) { results[i] = 0; }
        results[0] = 1;
        int a = 0, b = 0, c = 0;
        for (int i = 1; i < n; i++) {
            int l1 = results[a] * 2, l2 = results[b] * 3, l3 = results[c] * 5;
            results[i] = Math.min(Math.min(l1, l2), l3);
            if (l1 == results[i]) {
                a += 1;
            }
            if (l2 == results[i]) {
                b += 1;
            }
            if (l3 == results[i]) {
                c += 1;
            }
        }
        return results[n - 1];
    }
}
