# @title **TABLA DE MULTIPLICAR**

import time

tabla = 0
num = 0
while tabla < 13:
    print("")
    print("TABLA DEL", tabla, ":")
    time.sleep(0.3)
    while num < 13:
        print(tabla, "x", num, " =  ", tabla * num)
        num += 1
        time.sleep(0.3)
    tabla += 1
    num -= 13
