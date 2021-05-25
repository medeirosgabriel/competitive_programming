

public class Test {

	public static void main(String[] args) {
		
		TreeNode n10 = new TreeNode(-5, null, null);
		TreeNode n9 = new TreeNode(-5, null, null);
		TreeNode n8 = new TreeNode(-5, null, null);
		TreeNode n7 = new TreeNode(-5, null, null);
		TreeNode n6 = new TreeNode(-5, null, null);
                TreeNode n5 = new TreeNode(500, null, null);
                TreeNode n4 = new TreeNode(250, null, null);
                TreeNode n3 = new TreeNode(400, n4, n5);
		TreeNode n2 = new TreeNode(130, null, null);
                TreeNode n1 = new TreeNode(80, null, n2);
		TreeNode root = new TreeNode(120, n1, n3);

		System.out.println(Solution.maxSumBST(root));		
	}
}
