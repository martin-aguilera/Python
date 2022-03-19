from gtts import gTTS
from os import system

myText = input("Type something: ")
language = "en"

output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
system("start output.mp3")
