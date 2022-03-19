import requests, os
from bs4 import BeautifulSoup as bs

os.system("cls")

print("Type the url:")
url = input("")

r = requests.get(url)
soup = bs(r.text, "html.parser")
images = soup.find_all("img")
for image in images:
    print("\n")
    print(image["src"])
