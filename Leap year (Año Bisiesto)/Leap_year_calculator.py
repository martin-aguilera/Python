from os import system

system("cls")  # change 'cls' for 'clear' if u r using MacOS or Linux
print("\nWhat is the year?: ")
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It's a leap year", "\n")
else:
    print("It's not a leap year", "\n")
