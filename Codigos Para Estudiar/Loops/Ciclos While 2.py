import time

contador = 0

while (
    True
):  # Esta vez, el ciclo se ejecuta hasta que llegue a alguna condicion que la detenga.

    contador += 1  # Al contador se le suma 1 y continua el ciclo.
    time.sleep(0.01)  # Tiempo de espera para proceder a la siguiente instruccion.

    if contador == 1001:  # Si el contador llega a 1001,
        break  # el ciclo termina.

    else:  # Si el contador no es igual a 1001,
        print(contador)  # se imprime su numero actual.

print("El ciclo finalizó")  # Este mensaje se imprime una vez que finaliza el ciclo.
