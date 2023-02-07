palavra = input()
minuscula = 0
maiuscula = 0
for letra in palavra:
    if letra.islower():
        minuscula += 1
    else:
        maiuscula += 1
print(palavra.lower()) if minuscula >= maiuscula else print(palavra.upper())
