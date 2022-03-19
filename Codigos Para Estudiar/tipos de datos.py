"""TIPOS DE DATOS

Cadenas de texto (String) -> class str
Numericos:
 - Enteros -> class int
 - Flotantes -> class float
 - complejos -> class complex
Booleanos -> class bool

↓↓↓↓↓ Ejemplos ↓↓↓↓↓"""

###########
# 1 - String
a = "mensaje de prueba"
b = "b"
c = "12"
d = b + c
print(type(d))
print(d, "\n")

########
# 2 - Int
a = 1
b = 500
c = -999999999
d = a - b
print(type(d))
print(d, "\n")

##########
# 3 - Float
a = 0.5
b = 1.96
c = -1362.094
d = a * c
print(type(d))
print(d, "\n")

############
# 4 - Complex
a = 1j
b = 3 + 4j
c = 10 - 5j + 2
d = b * c
print(type(d))
print(d, "\n")

#########
# 5 - Bool
a = True
b = False
c = 2 + 2 == 4
d = 8 * 8 == 16
print(type(d))
print(d)
