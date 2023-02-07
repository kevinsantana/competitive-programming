qtd = int(input())
colunas = input().split()
colunas = [int(numero) for numero in colunas]
colunas.sort()
resultado = " ".join(str(coluna) for coluna in colunas)
print(resultado)
