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

import java.util.Arrays;

class Solution {

    public static int maxSumBST(TreeNode root) {
	int[] r = maxSumBSTAux(root);
	return r[0];
    }

    private static int[] maxSumBSTAux(TreeNode root) {
	
	int[] ret;

	if (root != null) {
                
		TreeNode l = root.left;
                TreeNode r = root.right;
                
		int[] sl = maxSumBSTAux(l);
                int[] sr = maxSumBSTAux(r);

		int hl = (sl[2] > root.val) ? sl[2] : root.val;
		int lr = (sr[3] < root.val) ? sr[3] : root.val;

		if (sl[1] != 0 && sr[1] != 0) {
			if (l != null && r != null) {
				if (sl[2] < root.val && sr[3] > root.val) {
					ret =  new int[] {root.val + sl[0] + sr[0], 1, hl, lr};
				} else {
                               		ret = new int[] {Math.max(sl[0], sr[0]), 0, hl, lr};
				}
			} else if (l != null) {
				if (sl[2] < root.val && sr[3] > root.val) {
                                        ret =  new int[] {root.val + sl[0], 1, hl, lr};
                                } else {
                                        ret = new int[] {Math.max(sl[0], sr[0]), 0, hl, lr};
                                }
			} else if (r != null) {
				if (sl[2] < root.val && sr[3] > root.val) {
                                        ret =  new int[] {root.val + sr[0], 1, hl, lr};
                                } else {
                                        ret = new int[] {Math.max(sl[0], sr[0]), 0, hl, lr};
                                }
               		} else {
				ret = new int[] {root.val, 1, hl, lr};
                	}
		} else {
			ret = new int[] {Math.max(sl[0], sr[0]), 0, hl, lr};
		}
        } else {
                ret = new int[] {0, 1, -1000000, 1000000}; 
        }
	
	System.out.println(Arrays.toString(ret));

	return ret;
    }
}
