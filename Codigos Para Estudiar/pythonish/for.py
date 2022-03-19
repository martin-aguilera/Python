"""
squares = []
for i in range(10):
    squares.append(i * i)
print(squares)
"""
from os import sep


squares = [i * i for i in range(10)]
print(squares)


"""
n = 3
for i in range(n):
    if n >= 0:
        print(i * i)
"""
n = 6
print([i * i for i in range(n) if n > 0])


n = 30
print([i + 1 for i in range(n) if n > 0])


a, b, c = 3, 4, 5
print(a, b, c, sep="")

for i in range(n):
    print(i)
