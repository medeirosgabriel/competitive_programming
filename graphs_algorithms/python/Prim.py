import heapq

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[0 for _ in range(V)] for _ in range(V)]

    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.adj[u][v] = w
        self.adj[v][u] = w

    def prim_mst(self):
        pq = []  # Priority queue to store vertices that are being processed
        src = 0  # Taking vertex 0 as the source

        # Create a list for keys and initialize all keys as infinite (INF)
        key = [float('inf')] * self.V

        # To store the parent array which, in turn, stores MST
        parent = [-1] * self.V

        # To keep track of vertices included in MST
        in_mst = [False] * self.V

        # Insert source itself into the priority queue and initialize its key as 0
        heapq.heappush(pq, (0, src))
        key[src] = 0

        # Loop until the priority queue becomes empty
        while pq:
            # The first vertex in the pair is the minimum key vertex
            # Extract it from the priority queue
            # The vertex label is stored in the second of the pair
            u = heapq.heappop(pq)[1]

            # Different key values for the same vertex may exist in the priority queue.
            # The one with the least key value is always processed first.
            # Therefore, ignore the rest.
            if in_mst[u]:
                continue

            in_mst[u] = True  # Include the vertex in MST

            # Iterate through all adjacent vertices of a vertex
            for v in range(self.V):
                weight = self.adj[u][v]
                if (weight > 0):
                    # If v is not in MST and the weight of (u, v) is smaller than the current key of v
                    if not in_mst[v] and key[v] > weight:
                        # Update the key of v
                        key[v] = weight
                        heapq.heappush(pq, (key[v], v))
                        parent[v] = u

        # Print edges of MST using the parent array
        print("Edges in the constructed MST")
        minimumCost = 0
        for i in range(1, self.V):
            par = parent[i]
            print(f"{par} -- {i} == {self.adj[i][par]}")
            minimumCost += self.adj[i][par]
        print("Minimum Spanning Tree", minimumCost)


# Driver program to test methods of the graph class
if __name__ == "__main__":
    V = 4
    g = Graph(V)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    g.prim_mst()