num1 = int(input("digita un numero: "))
num2 = int(input("digita otro numero: "))

resp = num1 + num2

print(num1, "+", num2, "=", num1 + num2)

if resp % 2 == 0:
    print(resp, "es un numero par")
else:
    print(resp, "es un numero inpar")
