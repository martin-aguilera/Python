"""
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

print(a, b, c)
"""

values = input("Enter space separated values:").split()
a, b, c = map(int, values)
print(a, b, c)
