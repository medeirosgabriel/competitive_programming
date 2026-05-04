"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.nodes = []
        if (root):
            self.bfs(root)
        
        n = len(self.nodes)
        if (n > 1):
            for i in range(1, n):
                t1, t2 = self.nodes[i - 1], self.nodes[i]
                n1, d1 = t1
                n2, d2 = t2
                if (d1 == d2):
                    n1.next = n2
                else:
                    n1.next = None

        return root

    def bfs(self, root):
        queue = [(root, 0)]
        while (queue):
            node, depth = queue.pop(0)
            self.nodes.append((node, depth))
            if (node.left):
                queue.append((node.left, depth + 1))
            if (node.right):
                queue.append((node.right, depth + 1))
