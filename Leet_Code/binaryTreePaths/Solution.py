# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def backtracking(self, node, curr):
        if (node != None):
            aux = curr + [str(node.val)]
            self.backtracking(node.right, aux)
            self.backtracking(node.left, aux)
            if (node.right == None and node.left == None):
                self.result.append("->".join(aux))

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        self.backtracking(root, [])
        return self.result
