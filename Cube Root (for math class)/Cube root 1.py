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

x = int(input("Enter an Integer: "))
ans = 0
while ans ** 3 < x:
    ans += 1
if ans ** 3 != x:
    print(f"{str(x)} is not a perfect cube")
else:
    print(f"Cube of root {str(x)} is {str(ans)}")
