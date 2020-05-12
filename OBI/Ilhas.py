# 90 pontos
from Queue import PriorityQueue

nos, arestas = map(int, raw_input().split())
maxn = nos + 2
lista_adj = [[] for i in range(maxn)]
lista_vis = [False] * maxn
pins = [10000000] * maxn

def dijsktra(start_node):
	mpq = PriorityQueue()
	pins[start_node] = 0
	mpq.put((0, start_node))
	while not mpq.empty():
		pin, node = mpq.get()
		lista_vis[node] = True
		for node_n, pin2 in lista_adj[node]:
			if not lista_vis[node_n] and pins[node_n] > pins[node] + pin2:
				pins[node_n] = pins[node] + pin2
				mpq.put((pins[node_n], node_n))

for i in range(arestas):
	a, b, dist = map(int, raw_input().split())
	lista_adj[a].append((b, dist))
	lista_adj[b].append((a, dist))
				
start_node = int(raw_input())
dijsktra(start_node)
pins.pop(start_node)
pins.pop(0)
pins.pop(len(pins) - 1)
saida = abs(max(pins) - min(pins))
print saida

