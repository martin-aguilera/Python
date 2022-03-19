# Aqui se hace una suma de las listas.

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 1, 1, 1, 1]

suma = list(map(lambda l1, l2: l1 + l2, lista1, lista2))
print(suma)
