# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, n):
        if (node.left == None and node.right == None):
            self.numbers.append(int(n + str(node.val)))
            return
        if (node.left != None): 
            self.dfs(node.left, n + str(node.val))
        if (node.right != None): 
            self.dfs(node.right, n + str(node.val))

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.numbers = []
        self.dfs(root, "")
        return sum(self.numbers)
