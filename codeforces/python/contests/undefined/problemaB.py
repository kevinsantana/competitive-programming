qtd = int(input())
problemas = 0
for _ in range(qtd):	
	problema = sum(map(int, input().split()))
	if problema >= 2:
		problemas += 1
print(problemas)