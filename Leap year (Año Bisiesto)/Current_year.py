import datetime
from os import system

system("cls")  # change 'cls' for 'clear' if u r using MacOS or Linux

year = datetime.datetime.now().strftime("%Y")
print("\nIt's the year", year)
if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
    print("It's a leap year", "\n")
else:
    print("It's not a leap year", "\n")
