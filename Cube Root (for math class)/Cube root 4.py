print("\nExamples:")
print("0 ** 3" + " = " + str(0 ** 3))
print("1 ** 3" + " = " + str(1 ** 3))
print("2 ** 3" + " = " + str(2 ** 3))
print("3 ** 3" + " = " + str(3 ** 3))
print("4 ** 3" + " = " + str(4 ** 3))
print("5 ** 3" + " = " + str(5 ** 3))
print("6 ** 3" + " = " + str(6 ** 3))
print("7 ** 3" + " = " + str(7 ** 3))
print("8 ** 3" + " = " + str(8 ** 3))
print("9 ** 3" + " = " + str(9 ** 3))
print("\n")

cube = int(input("Type an integer: "))

for guess in range(abs(cube) + 1):
    if guess ** 3 >= abs(cube):
        break
if guess ** 3 != abs(cube):
    print(str(cube), "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("Cube root of", str(cube), "is", str(guess))
