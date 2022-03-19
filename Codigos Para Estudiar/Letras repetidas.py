from os import system

system("cls")

count = 0

text = (input("Escribe algo: ")).lower()
word = (input("Escribe la letra que quieras revisar: ")).lower()

for wea in text:
    if wea.isalpha():
        if word == wea:
            count += 1
if count == 1:
    print(f"La letra '{word}' aparece {count} vez")
else:
    print(f"La letra '{word}' aparece {count} veces")
