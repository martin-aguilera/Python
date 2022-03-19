import time

print("Para continuar debes crear una contraseña", "\n")
time.sleep(0.5)
pass_1 = input("Ingresa tu contraseña: ")
time.sleep(0.1)
pass_2 = input("Repite tu contraseña: ")
time.sleep(0.1)

if pass_1 == pass_2:
    print("\n", "Tu contraseña es", pass_1)
    print("tu contraseña posee", len(pass_1), "digitos")

while pass_1 != pass_2:
    time.sleep(0.5)
    print("\n", "Por favor ingresa bien tu contraseña", "\n")
    time.sleep(0.3)
    pass_1 = input("Ingresa tu contraseña: ")
    time.sleep(0.1)
    pass_2 = input("Repite tu contraseña: ")
    time.sleep(0.5)

    if pass_1 == pass_2:
        print("Tu contraseña es", pass_1)
        print("tu contraseña posee", len(pass_1), "digitos")
        time.sleep(0.5)
        break
    else:
        print("\n", "Noooooo")
        time.sleep(0.5)
        continue
