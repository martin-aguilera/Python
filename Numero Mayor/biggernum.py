a = int(input('\nnumero "a": '))
b = int(input('numero "b": '))
c = int(input('numero "c": '))
if a > b and a > c:
    print(f'en numero mayor es "a": {a}')
elif b > a and b > c:
    print(f'en numero mayor es "b": {b}')
else:
    print(f'en numero mayor es "c": {c}')
