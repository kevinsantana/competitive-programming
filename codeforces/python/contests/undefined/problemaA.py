limak, bob = map(int, input().split())
qtd_anos = 0
while limak <= bob:
    limak = limak * 3
    bob = bob * 2
    qtd_anos = qtd_anos + 1
print(qtd_anos)
