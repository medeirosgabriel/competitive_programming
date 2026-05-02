# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.queue = []
        max_depth = self.bfs(root, 0)
        self.answer = [[] for _ in range(max_depth)]
        while self.queue:
            e, d = self.queue.pop(0)
            self.answer[d].append(e)
        return self.answer

    def bfs(self, node, depth):
        if (node != None):
            self.queue.append((node.val, depth))
            d1 = self.bfs(node.left, depth + 1)
            d2 = self.bfs(node.right, depth + 1)
            return max(d1, d2)
        else:
            return depth

