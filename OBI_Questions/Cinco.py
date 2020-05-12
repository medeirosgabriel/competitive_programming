# 100 pontos
n = int(raw_input())
numeros = map(int, raw_input().split())
if 0 not in numeros and 5 not in numeros:
	print -1
else:
	troca = False
	for i in range(len(numeros)):
		if (numeros[i] == 5 or numeros[i] == 0):
			if numeros[i] <= numeros[len(numeros) - 1]:
				numeros[len(numeros) - 1], numeros[i] = numeros[i], numeros[len(numeros) - 1]
				troca = True
				break
	if troca == False:
		for i in range(len(numeros) -1, -1, -1):
			if numeros[i] == 5 or numeros[i] == 0:
				numeros[len(numeros) - 1], numeros[i] = numeros[i], numeros[len(numeros) - 1]
				break
	for e in numeros:
		print e,
