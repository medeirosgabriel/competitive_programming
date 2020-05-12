
def find(a): #Procura representante de a
	if parent[a] == a:
		return a
	parent[a] = find(parent[a]) 
	return parent[a]

def join(parent1, parent2): #Junta dois grupos
	if parent1 != parent2:
		parent[parent1] = parent2

maxn = 100
nodes, edges = map(int, raw_input().split())
parent = [ i for i in xrange(maxn) ] # IMPORTANTE - Inicia representante de cada grupo como sendo si proprio
edges_graph = []

for i in xrange(edges):
    city1, city2, cost_road = map(int, raw_input().split())
    edges_graph.append( (cost_road, city1, city2) )

edges_graph.sort() #Ordena arestas pelo custo

sum_cost = 0
for cost_road, city1, city2 in edges_graph:
	parentCity1 = find(city1)
	parentCity2 = find(city2)

	if parentCity1 != parentCity2:
		sum_cost += cost_road
		join(parentCity1, parentCity2)

print parent
print sum_cost