# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.output = []
        
    def walk(self, node, values, targetSum):
        if (node != None):
            values.append(node.val)
            #print(values, sum(values))
            if (sum(values) == targetSum):
                self.output.append(values[:])
            if (node.left != None):
                self.walk(node.left, values, targetSum)
                values.pop()
            if (node.right != None):
                self.walk(node.right, values, targetSum)
                values.pop()
                
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.walk(root, [], targetSum)
        return self.output
