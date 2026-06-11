# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, sum_):
        if (node):
            val = node.val
            if (not node.left and not node.right):
                return sum_ + val == self.targetSum
            else:
                return self.dfs(node.left, sum_ + val) or self.dfs(node.right, sum_ + val)
        else: 
            return False

    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        self.targetSum = targetSum
        if (not root): return False
        return self.dfs(root, 0)

