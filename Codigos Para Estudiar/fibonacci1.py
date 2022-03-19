print("ingresa un numero:")
num = int(input())


def fib(n):
    a = 0
    b = 1

    for i in range(n):
        c = a + b
        a = b
        b = c
    return b


for j in range(10):
    print(fib(j))
