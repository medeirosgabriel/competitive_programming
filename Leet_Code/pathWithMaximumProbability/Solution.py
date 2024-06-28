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
        inf = float("inf")
        adj = [[] for i in range(n)]
        visited = [False] * n
        probs = [-1] * n
        probs[start_node] = 1

        for i in range(len(edges)):
            a, b = edges[i]
            succ = succProb[i]
            adj[a].append((b, succ))
            adj[b].append((a, succ))
        
        queue = PriorityQueue()
        visited[start_node] = True
        queue.put((1, start_node))
        while (not queue.empty()):
            _, node = queue.get()
            visited[node] = True
            for node_n, prob_n in adj[node]:
                if not visited[node_n] and probs[node] * prob_n > probs[node_n]:
                    probs[node_n] = probs[node] * prob_n
                    queue.put((probs[node_n] * -1, node_n))

        resp = probs[end_node]
        return 0 if (resp == -1) else resp
