# Serie Fibonacci


import time

finalserie = int(input("ingresa el número en el que termina la serie fibonacci   "))
num1 = 0
num2 = 1
while num1 < finalserie:
    num2 = num1 + num2
    num1 = num2 - num1
    print("He aquí la serie fibonaci " + str(num1), end=time.sleep(0.4))


print("fin")
