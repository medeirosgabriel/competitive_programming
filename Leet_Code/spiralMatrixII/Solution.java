class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int element = 1, left = 0, top = 0, right = n - 1, bottom = n - 1;
        while (left <= right && top <= bottom) {
            for (int i = left; i <= right; i++) {
                matrix[top][i] = element++;
            }
            top++;

            for (int i = top; i <= bottom; i++) {
                matrix[i][right] = element++;
            }
            right--;

            for(int i = right; i >= left; i--){
                matrix[bottom][i] = element++;
            }
            bottom--;

            for(int i = bottom; i >= top; i--){
                matrix[i][left] = element++;
            }
            left++;
        }
        return matrix;
    }
}
