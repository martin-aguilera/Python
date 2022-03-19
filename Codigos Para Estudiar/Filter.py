# Con este codigo se pueden filtrar
# los los numeros pares en la lista.

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

pares = list(filter(lambda numero: numero % 2 == 0, numeros))
print(numeros)
print(pares, "\n")
