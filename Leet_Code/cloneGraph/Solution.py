"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def dfs(self, node):
        if (not node.val in self.visited):
            self.visited[node.val] = Node(node.val, [])
            for ng in node.neighbors:
                self.dfs(ng)
                self.visited[node.val].neighbors.append(self.visited[ng.val])

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.visited = {}
        if (node != None):
            self.dfs(node)
            return self.visited[1]
        return None
