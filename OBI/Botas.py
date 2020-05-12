# 100 PONTOS
n = int(raw_input())
dicionario = {}
for i in range(n):
	dados = raw_input().split()
	if dados[0] not in dicionario:
		if dados[1] == "D":
			dicionario[dados[0]] = [1, 0]
		if dados[1] == "E":
			dicionario[dados[0]] = [0, 1]
	else:
		if dados[1] == "D":
			dicionario[dados[0]][0] += 1
		if dados[1] == "E":
			dicionario[dados[0]][1] += 1
quant = 0
for e in dicionario.values():
	if e[0] == e[1]:
		quant += e[0]
	else:
		diferenca = abs(e[0] - e[1])
		quant += max(e) - diferenca
print quant
