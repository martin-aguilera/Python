from os import system

system("cls")
print("Enter a number:")
cube = float(input())
epsilon = 0.01
guess = 0.0
increment = 0.001
num_guesses = 0

while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print("num_guesses = ", num_guesses)
if abs(guess ** 3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is close to the cube root of", cube)
    print(guess, "rounded is", round(guess))
