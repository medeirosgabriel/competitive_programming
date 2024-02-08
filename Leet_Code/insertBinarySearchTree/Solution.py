# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, last, val, pos):
        if (node == None):
            if (pos == "l"):
                last.left = TreeNode(val, None, None)
            else:
                last.right = TreeNode(val, None, None)
            return
        if (val <= node.val):
            self.dfs(node.left, node, val, 'l')
        else:
            self.dfs(node.right, node, val, 'r')

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if (root != None):
            self.dfs(root, None, val, None)
        else:
            root = TreeNode(val, None, None)
        return root
