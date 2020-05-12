import Queue

maxn = 100

lst_adj = [ [] for i in xrange(maxn) ]
nodes_visited = [False] * maxn
distance = [-999] * maxn

def bfs(start_node):
	distance[start_node] = 0
	nodes_visited[start_node] = True
	my_queue = Queue.Queue()
	my_queue.put(start_node)
	while not my_queue.empty():
		node = my_queue.get()
		for node_neigh in lst_adj[node]:
			if not nodes_visited[node_neigh]:
				nodes_visited[node_neigh] = True
				distance[node_neigh] = distance[node] + 1
				my_queue.put(node_neigh)


nodes, edges = map(int, raw_input().split())

for i in xrange(edges):
	city1, city2 = map(int, raw_input().split())
	lst_adj[city1].append(city2)
	lst_adj[city2].append(city1)

start_node = int(raw_input())
bfs(start_node)

print distance