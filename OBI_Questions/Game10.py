# 100 pontos
n = int(raw_input())
pdv = int(raw_input())
pa = int(raw_input())
if pdv < pa:
	saida = abs(n - pa + pdv)
	print saida
else:
	saida = pdv - pa
	print saida
