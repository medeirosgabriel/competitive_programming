class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if n == 1:
            return [0]

        self.graph = [set() for _ in range(n)]

        for e1, e2 in edges:
            self.graph[e1].add(e2)
            self.graph[e2].add(e1)
        
        leaves = [i for i in range(n) if len(self.graph[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = self.graph[leaf].pop()
                self.graph[neighbor].remove(leaf)
                if len(self.graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves

        return leaves
        
