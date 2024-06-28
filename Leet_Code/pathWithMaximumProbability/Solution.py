from Queue import PriorityQueue

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            a,b = edges[i]
            prob = succProb[i]
            adj[a].append((b, prob))
            adj[b].append((a, prob))

        probs = [0] * n
        visited = [False] * n
        probs[start_node] = 1
        queue = PriorityQueue()
        queue.put((1, start_node))
        while(not queue.empty()):
            _, node = queue.get()
            visited[node] = True
            for node_n, prob in adj[node]:
                if (not visited[node_n] and probs[node] * prob > probs[node_n]):
                    probs[node_n] = probs[node] * prob
                    queue.put((probs[node] * prob * -1, node_n))
                    
        return probs[end_node]
