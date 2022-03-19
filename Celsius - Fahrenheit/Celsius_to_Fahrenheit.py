from os import system as sys

sys("cls")


def function(C):
    F = C * 1.8 + 32
    return str(C) + "°C = " + str(F) + "°F"


print("Ingrese la temperatura en Celsius:")
print(function(float(input())))
