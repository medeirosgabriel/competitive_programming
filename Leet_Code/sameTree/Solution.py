# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, t1, t2):
        if (t1 == None or t2 == None):
            if (t1 == t2): return True
            else: return False
        if (t1.val == t2.val):
            left = self.dfs(t1.left, t2.left)
            right = self.dfs(t1.right, t2.right)
            return True and left and right
        else:
            return False

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.dfs(p, q)
