from random import choice

name = input("Your name: ")
last_name = input("Your last name: ")

print(f"Your name is {name} {last_name}")

Players = ["Mario", "Pikachu", "Megaman", "Donkeykong", "Charizard"]

Player_Choice = choice(Players)

print(f"{name}, your character will be: {Player_Choice}")
