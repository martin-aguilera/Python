"""
username = input('Enter Username: ')
password = input('Enter Password: ')
"""

from getpass import getpass

username = input("Enter Username: ")
password = getpass("Enter Password: ")


# test the password
if password == "darckar1" and username == "exaiden":
    print("-LogIn Succesfully-")
else:
    print("Wrong user or password")
