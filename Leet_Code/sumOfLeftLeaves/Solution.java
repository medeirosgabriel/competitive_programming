/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int getSum(TreeNode node, boolean left) {
        if (node.left == null && node.right == null) {
            if (left) {
                return node.val;
            }
            return 0;
        } else {
            int sum = 0;
            if (node.left != null) {
                sum += getSum(node.left, true);
            }
            if (node.right != null) {
                sum += getSum(node.right, false);
            }
            return sum;
        }
    }
    public int sumOfLeftLeaves(TreeNode root) {
        return getSum(root, false);
    }
}
