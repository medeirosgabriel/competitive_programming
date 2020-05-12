from Queue import Queue

dx = (0, 0, 1, -1) # Movimento no eixo x
dy = (1, -1, 0, 0) # Movimento no eixo y

def verify_position(x, y):
	return (x >= 0 and x < m and y >= 0 and y < n)

def bfs_in_grid(start_x, start_y):
	distance[start_x][start_y] = 0
	visited[start_x][start_y] = True
	my_queue = Queue()
	my_queue.put( (start_x, start_y) )

	while not my_queue.empty():
		x, y = my_queue.get()

		for i in xrange(4):
			new_x = x + dx[i]
			new_y = y + dy[i]
			if verify_position(new_x, new_y) and matriz[new_x][new_y] != '#' and not visited[new_x][new_y]:
				distance[new_x][new_y] = distance[x][y] + 1
				visited[new_x][new_y] = True
				my_queue.put( (new_x, new_y) )

n, m = map(int, raw_input().split()) # Dimensao do grid n x m
matriz = [ [] for i in xrange(n) ] # Cria uma matriz coluna para representar o grafo com tamanho maxnm x 1
distance = [ [-999] * m for i in xrange(n) ] # Cria uma matriz que representa a distancia com tamanho n x m
visited = [ [False] * m for i in xrange(n) ] # Cria uma matriz de visitados com tamanho n x m

for line in xrange(n):
	matriz[line] = raw_input().split() 	# Le a linha da matriz a adiciona para 
										# representar o grafo (considere o valor de cada celula passando com espaco)

start_x, start_y = map(int, raw_input().split())
bfs_in_grid(start_x, start_y)

for line in xrange(n):
	print distance[line]