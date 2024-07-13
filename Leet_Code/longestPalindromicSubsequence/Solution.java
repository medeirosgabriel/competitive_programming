class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length(), max = 1;
        int[][] dp = new int[n][n];
        for (int r = 0; r < n; r++) { // End string
            dp[r][r] = 1;
            for (int l = r - 1; l >= 0; l--) { // Start String
                if (s.charAt(r) == s.charAt(l)) {
                    dp[r][l] = dp[r - 1][l + 1] + 2;
                    max = Math.max(max, dp[r][l]);
                } else {
                    dp[r][l] = Math.max(dp[r - 1][l], dp[r][l + 1]);
                }
            }
        }
        return max;
    }
}
