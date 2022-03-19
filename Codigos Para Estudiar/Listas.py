# Crear la lista:
mi_lista = [0, 1, 2, 3, 4, 5]
mi_otra_lista = [["a", "b", "c"], [1, 2, 3], [True, False], mi_lista]
print("\n", type(mi_lista), "\n")

# Imprimir la lista:
print("La lista:")
print(mi_lista, "\n")

# Imprimir un elemento especifico de la lista:
print("Elemento especifico de la lista:")
print(mi_lista[2])
print(mi_lista[3], "\n")

# Editar un elemento de la lista e imprimirla:
print("Un elemento de la lista editado:")
mi_lista[5] = 21j
print(mi_lista, "\n")

# Imprimir el ultimo elemento de la lista:
print("El ultimo elemento de la lista es:")
print(mi_lista[-1], "\n")

# Imprimir un rangos de elementos de la lista:
print("Se imprime desde ciertos rangos de la lista:")
print(mi_lista[1:4])
print(mi_lista[2:-1], "\n")

# Imprimir una lista que contiene listas:
print("Listas dentro de una lista:")
print(mi_otra_lista, "\n")

# Imprimir un elemento especifico de una lista dentro de otra lista:
print("Elemento especifico de una lista dentro de otra lista:")
print(mi_otra_lista[2][0], "\n")

# Agregar un nuevo elemento a la lista:
print("El nuevo elemento agregado va al final de la lista:")
mi_lista.append(999)
mi_lista.append(70000)
print(mi_lista, "\n")

# Agregar un nuevo elemento a la lista en una posicion especifica:
print("Nuevo elemento en una posicion especifica de la lista:")
mi_lista.insert(0, -1)
mi_lista.insert(1, 0.5)
mi_lista.insert(3, "hola")
mi_lista.insert(4, "hola")
print(mi_lista, "\n")

# Eliminar el ultimo elemento de la lista:
print("Eliminar el ultimo elemento de la lista")
mi_lista.pop()
print(mi_lista, "\n")

# Eliminar una pocicion especifica:
print("Eliminar una pocicion especifica de la lista:")
mi_lista.pop(5)
print(mi_lista, "\n")

# Eliminar un elemento en especifico:
print("Eliminar un elemento por su nombre, no por su pocicion:")
mi_lista.remove(0.5)
print(mi_lista, "\n")

# Cuantos elementos tiene la lista:
print("¿Cuantos elementos tiene la lista?:")
xd = len(mi_lista)
print(xd)

# Cuantos elementos se repiten:
print("¿Se repite algun elemento en la lista?:")
dx = mi_lista[2]
xd = mi_lista.count(dx)
print('"' + dx + '"', "se repite", xd, "veces" "\n")

# Indicar en que posicion se encuentra cierto elemento:
print("Indica la posicion de cierto elemento:")
xd = mi_lista.index(3)
print('"' + mi_lista[3] + '"', "está en la posicion", xd, "\n")
