# En este codigo se imprimen todos los
# numeros que sean menores que 501

from os import system
from time import (
    sleep,
)  # Para poder usar un tiempo de espera entre los numeros que se imprimiran.

system("cls")
i = 0  # El numero actual la variable 'contador' es Cero.
while i < 501:  # Esto estara trabajando Mientras el contador sea menor que 501.
    print(i)  # Primero se imprime el numero actual que posee la variable 'contador'.
    i += 1  # Despues a 'contador' se le suma 1.
    sleep(0.5)  # Este es el tiempo de espera para proceder al siguiente trabajo.

# Ya que no hay nada mas que hacer aqui, el 'while' vuelve al proceso del 'print', pero
# esta vez imprimirá la variable con un nuevo numero.
