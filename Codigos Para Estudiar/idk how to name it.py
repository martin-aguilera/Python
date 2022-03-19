MIT = "asewiyoqul"
numVowels = 0

for char in MIT:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        numVowels += 1
        print(char)

print("Number of Vowels: " + str(numVowels))
