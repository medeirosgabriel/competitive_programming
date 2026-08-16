# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution(object):

    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        dq = deque([])
        dq.append(root)
        while dq:
            node = dq.popleft()
            if (node.right): dq.append(node.right)
            if (node.left): dq.append(node.left)
        return node.val

