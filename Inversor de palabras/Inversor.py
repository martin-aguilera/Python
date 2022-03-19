# from os import system
# from time import sleep

# system("cls")
# print("\n")


# def Normal():
#     count_word = ""
#     new_word = ""
#     print("Escribe algo:")
#     normal_word = input("")
#     longitud = len(normal_word)
#     sleep(1)
#     print(f"\nLa palabra {normal_word} posee", len(normal_word), "letras\n")
#     for letra in normal_word:
#         count_word += letra

#         sleep(0.35)
#         system("cls")
#         print(f"\nLa palabra {normal_word} posee", longitud, "letras\n")
#         print("\nPalabra normal:       ", count_word, "\n")
#         print("\nPalabra invertida:    ", count_word[::-1], "\n")
#     sleep(0.35)
# Normal()

S = input("")
print(S[::-1])
