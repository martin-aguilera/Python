# Este codigo permite sumar
# todos los datos de una lista
# (tambien sirve con cadenas de texto)

from functools import reduce

lista = [2, 4, 6, 8, 10]
redu = reduce(lambda x, y: x + y, lista)
print(redu)
