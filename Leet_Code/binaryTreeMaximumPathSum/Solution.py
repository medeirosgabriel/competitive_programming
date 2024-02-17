# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def dfs(self, node):
        if (node == None):
            return 0
        sum_l = max(0, self.dfs(node.left))
        sum_r = max(0, self.dfs(node.right))
        curr = node.val + sum_l + sum_r
        self.max_path = max(self.max_path, curr)
        return node.val + max(sum_l, sum_r)
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path = float("-inf")
        self.dfs(root)
        return self.max_path
