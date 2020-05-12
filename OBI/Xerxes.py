# 100 pontos
lista_adj = [[1, 2], [2, 3], [3, 4], [0, 4], [0, 1]]
dario = 0
xerxes = 0
n = int(raw_input())
for i in range(n):
	d, x = map(int, raw_input().split())
	if x in lista_adj[d]:
		dario += 1
	else:
		xerxes += 1
if dario > xerxes:
	print "dario"
else:
	print "xerxes"
