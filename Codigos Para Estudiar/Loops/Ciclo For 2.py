# En este codigo se imprime cada elemento del diccionario.

import time

lista = {"weon 1": 1000, "weon 2": 2000, "weon 3": 3000, "weon 4": 4000, "weon 5": 5000}

for weones, numeros in lista.items():
    print(weones + ": " + str(numeros))
    time.sleep(0.5)
