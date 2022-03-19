num1 = 10  # es un int
num2 = -5  # es un int
num3 = 0.5  # es un float
num4 = 7.3  # es un float
num5 = 4j  # en un complex
num6 = 2 + 1j  # es un complex
txt1 = "Sacowea"  # es un str
txt2 = "56"  # es un str

# Para imprimir el tipo de dato se usa:
print(type(num2), type(num4), type(num6), type(txt2))
print(num2, num4, num6, txt2, "\n")

# Para cambiar el tipo de dato de numero a texto se usa:
print(type(str(num2)), type(str(num6)), type(str(num4)))
print(str(num2) + " " + str(num6) + " " + str(num4) + "\n")

# Para cambiar el tipo de dato de texto a numero se usa:
print(type(int(txt2)))
print(int(txt2))
