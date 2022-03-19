""" Las tuplas, a diferencia de una lista, sus datos se guardan en parentesis y
	no en corchetes, ademas que no se pueden editar los datos que poseen, pero
	el resto se puede usar de igual manera que una lista. 
	Puedes ver el archivo Listas.py para ver todo lo que se puede hacer porque
	 me da paja escribir todo de nuevo. """

tupla = (0, 1, 2, "a", "b", "c", True, False, 0)
print("\n", type(tupla), "\n")
print(tupla, "\n")

print(tupla[5])
print(tupla[2])
print(tupla[-1], "\n")

print(tupla[1:4])
print(tupla[2:6], "\n")

print(tupla[:4])
print(tupla[:7], "\n")

print(len(tupla), "\n")

print(tupla.count(0), "\n")
