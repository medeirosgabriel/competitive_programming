class Solution {
    public boolean isValidSudoku(char[][] board) {
        int n = board.length;
        Set<String> seen = new HashSet<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] != '.') {
                    String c = "(" + board[i][j] + ")";
                    String v1 = i/3 + c + j/3;
                    String v2 = String.valueOf(i) + c;
                    String v3 = c + String.valueOf(j);
                    if (!seen.add(v1) || !seen.add(v2) || !seen.add(v3)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
