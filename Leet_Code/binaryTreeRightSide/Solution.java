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

import java.util.List;
import java.util.LinkedList;

class Solution {

	public static List<Integer> rightSideView(TreeNode root) {
		List<Integer> list = new LinkedList<>();
		if (root != null) {
			list.add(root.val);
			rightSideView(root.right, list);
		}
		return list;
	}

	private static void rightSideView(TreeNode root, List<Integer> list) {
		if (root != null) {
			rightSideView(root.left, list);
			list.add(root.val);
			rightSideView(root.right, list);
		}

	}

	
}
