def func(lista, i = 0, j = -1):
    if j == -1:
        j = len(lista)

    if i < j:
        func(lista, i+1, j)

        elem = lista[i]
        k = i + 1

        while k < j and elem  > lista[k]:
            lista[k-1] = lista[k]
            k += 1

        lista[k-1] = elem

if __name__ == "__main__":
    lista = [3,3,2,1,4]
    print(func(lista))
