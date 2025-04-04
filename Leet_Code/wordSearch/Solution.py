class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                boolean result = dfs(board, i, j, 0, word);
                if (result) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean dfs(char[][] board, int i, int j, int p, String target) {
        if (p == target.length()) return true;
        if (i < 0 || i >= board.length || j < 0 || j >= board[i].length || board[i][j] != target.charAt(p)) return false;
        char temp = board[i][j];
        board[i][j] = ' ';
        boolean result = dfs(board, i + 1, j, p + 1, target) || dfs(board, i - 1, j, p + 1, target) || 
                         dfs(board, i, j + 1, p + 1, target) || dfs(board, i, j - 1, p + 1, target);
        if (result) return true;
        board[i][j] = temp;
        return false;
    }
}
