from time import sleep
import os

delay = 0.1
count = 0

while count < 20:
    os.system("cls")
    print("\n", " / Cargando | ", "\n")
    sleep(delay)
    os.system("cls")
    print("\n", " ― Cargando / ", "\n")
    sleep(delay)
    os.system("cls")
    print("\n", " \ Cargando ― ", "\n")
    sleep(delay)
    os.system("cls")
    print("\n", " | Cargando \ ", "\n")
    sleep(delay)
    count += 1
os.system("cls")
print("\nLISTO\n")
sleep(0.5)
print("CLOSING...")
sleep(0.5)
os.system("exit")
