class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self

class UnionFind:
    def find(self, node):
        if (node.parent != node):
            return self.find(node.parent)
        return node
    
    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if (parent1 != parent2):
            parent2.parent = parent1
        return parent1

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        parents = {}
        uf = UnionFind()
        n = len(isConnected)
        count = 0
        for i in range(n):
            for j in range(n):
                if (j >= i):
                    edge = isConnected[i][j]
                    if (edge == 1):
                        if (i != j):
                            if (not i in parents):
                                parents[i] = Node(i)
                            if (not j in parents):
                                parents[j] = Node(i)
                            parent1 = uf.find(parents[i])
                            parent2 = uf.find(parents[j])
                            if (parent1 != parent2):
                                uf.union(parent1, parent2)
                                count -= 1
                        else:
                            if (not i in parents):
                                parents[i] = Node(i)
                            count += 1
        return count
