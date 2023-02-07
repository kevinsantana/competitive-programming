qtd = int(input())
imas = ""
transicao = 0
for _ in range(qtd):
    imas += input()
if "11" in imas:
    transicao += 1
if "00" in imas:
    transicao += 1
print(transicao + 1)
