from os import system as sys

sys("cls")


def function(F):
    C = (F - 32) / 1.8
    return str(F) + "°F = " + str(C) + "°C"


print("Ingrese la temperatura en Fahrenheit:")
print(function(float(input())))
