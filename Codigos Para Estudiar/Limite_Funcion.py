"""
Se nos dice que "S" es una lista finita de numeros y f(x) es ((x ** 4) - (x ** 2)) / ((x ** 3) + (3 * x)).
Recuerda que cada elemento "S" es una x.
Tambien se nos dice que el resultado deberia ser [-30/7, -60/19, -2, -6/7, 0, 0, 6/7, 2, 60/19, 30/7].
"""

S = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
should_be = [-30 / 7, -60 / 19, -2, -6 / 7, 0, 0, 6 / 7, 2, 60 / 19, 30 / 7]
result = []


def f(x):
    f = ((x ** 4) - (x ** 2)) / ((x ** 3) + (3 * x))
    return f


for x in S:
    result.append(f(x))
print(
    f"\nThe result and f(x) are the same?\n\nresult = {result}\nf(x)   = {should_be}\n\n{should_be == result}\n"
)
