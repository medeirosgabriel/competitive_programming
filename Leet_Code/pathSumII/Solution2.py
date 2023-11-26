# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def dfs(self, node, result, nodes, sum_, targetSum):
        if (node != None):
            v = node.val
            nodes.append(v)
            total = sum_ + v
            isLeaf = (node.left == None and node.right == None)
            if (isLeaf and total == targetSum):
                result.append(list(nodes))
            else:
                self.dfs(node.left, result, nodes, total, targetSum)
                self.dfs(node.right, result, nodes, total, targetSum)
            nodes.pop()
            
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result, nodes = [], []
        self.dfs(root, result, nodes, 0,  targetSum)
        return result 
