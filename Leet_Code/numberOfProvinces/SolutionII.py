class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        self.visited = set()
        self.n = len(isConnected)
        self.isConnected = isConnected
        provinces = 0

        for i in range(self.n):
            if not i in self.visited:
                self.bfs(i)
                provinces += 1
        return provinces
		

    def bfs(self, node):
        queue = deque([node])
        self.visited.add(node)
		
        while queue:
            curr_node = queue.popleft()
            for j in range(self.n):
                if self.isConnected[curr_node][j] == 1 and not(j in self.visited):
                    queue.append(j)
                    self.visited.add(j)		
