class Solution(object):

    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        root_answer = 0
        subtree = {}
        
        def dfs(node, prev, depth):
            total = 1
            nonlocal root_answer
            root_answer += depth
            for child in graph[node]:
                if (child != prev):
                    total += dfs(child, node, depth + 1)
            subtree[node] = total
            return total
        
        dfs(0, None, 0)
        res = [0] * n
        res[0] = root_answer

        def dfs2(node, prev):
            for child in graph[node]:
                if (child != prev):
                    res[child] = res[node] - subtree[child] + (n - subtree[child])
                    dfs2(child, node)
        
        dfs2(0, None)
        return res


        

        
