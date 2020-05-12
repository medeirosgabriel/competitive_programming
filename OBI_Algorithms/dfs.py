def dfs(node):
	nodes_visited[node] = True
	for node_neigh in lst_adj[node]:
		if nodes_visited[node_neigh] == False:
			dfs(node_neigh)

maxn = 100

lst_adj = [ [] for i in xrange(maxn) ]
nodes_visited = [False] * maxn

nodes, edges = map(int, raw_input().split())

for i in xrange(edges):
	city1, city2 = map(int,raw_input().split())
	lst_adj[city1].append(city2)
	lst_adj[city2].append(city1)

start_node = int(raw_input())

dfs(start_node)

print nodes_visited