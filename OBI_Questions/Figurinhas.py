# 100 pontos
n, c, m = map(int, raw_input().split())
fig_car = map(int, raw_input().split())
fig_comp = map(int, raw_input().split())
faltam = c
for e in fig_car:
	if e in fig_comp:
		faltam -= 1
print faltam
