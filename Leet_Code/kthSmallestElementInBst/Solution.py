# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def dfs(self, node):
        if (node != None):
            self.dfs(node.left)
            self.k -= 1
            if (self.k == 0):
                self.result = node.val
                return
            self.dfs(node.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k, self.result = k, -1
        self.dfs(root)
        return self.result
        
