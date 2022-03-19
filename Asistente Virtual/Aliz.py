import pyttsx3, pywhatkit, urllib.request, json, datetime, pyjokes, wikipedia, subprocess, pyautogui  # bluetooth,
import speech_recognition as sr
from os import system
from joke_generator import generate
from random import choice

system("cls")

jokes = [pyjokes.get_joke(), generate()]
key = "AIzaSyCYEQsjqR1Y0V9KhVgNP7uiCegeAdhYFsw"
name = "alexa"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")


engine.setProperty("voice", voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


# def Bluetooth():
# try:
# nearby_devices = bluetooth.discover_devices(lookup_names=True)
# system('cls')
# print("\nI Found %d devices nearby" % len(nearby_devices))
# talk("\nI Found %d devices nearby" % len(nearby_devices))
# if len(nearby_devices) == 0:
# print('Check if you have bluetooth activated or if there is something interfering with the signal')
# talk('Check if you have bluetooth activated or if there is something interfering with the signal')
# except:
# system('cls')
# print('An error has occurred. please check your bluetooth connection and try again')
# talk('An error has occurred. please check your bluetooth connection and try again')

# for addr, name in nearby_devices:
# print("  %s - %s" % (addr, name))


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if name in command:
                command = command.replace(name, "")
                print(command)
    except:
        pass

    return command


def run_alexa():
    command = take_command()
    system("cls")
    print(command)

    if "introduce yourself" in command:
        print(f"\nHi there!, my name is {name}")
        talk(f"Hi there!, my name is {name}")
        print("I am a virtual assistant that has not been finished yet")
        talk("I am a virtual assistant that has not been finished yet")
        print("I hope i can be usefull someday")
        talk("I hope i can be usefull someday")

    elif "play on youtube" in command:
        song = command.replace("play", "")
        print(f"playing {song}")
        talk(f"playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Current time is {time}")
        talk(f"Current time is {time}")

    elif "search for" in command:
        search = command.replace("search for", "")
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)

    elif "date" in command:
        print("sorry, I have a headache")
        talk("sorry, I have a headache")

    elif "are you single" in command:
        print("I am in a relationship with wifi")
        talk("I am in a relationship with wifi")

    elif "joke" in command:
        joke = choice(jokes)
        print(joke)
        talk(joke)

    elif "open" in command:
        prog = command.replace("open", "")
        if "notepad" in prog:
            print("\nOpening Notepad")
            talk("Opening Notepad")
            subprocess.Popen("C:\\WINDOWS\\system32\\notepad.exe")
        elif "steam" in prog:
            print("\nOpening Steam")
            talk("Opening Steam")
            subprocess.Popen("C:\\Program Files (x86)\\Steam\\steam.exe")
        elif "calculator" in prog:
            print("\nOpening Calculator")
            talk("Opening Calculator")
            subprocess.Popen("C:\\WINDOWS\\system32\\calc.exe")
        elif "opera" in prog:
            print("\nOpening Opera")
            talk("Opening Opera")
            subprocess.Popen(
                "C:\\Users\\e x a i d e n\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            )
        elif "osu" in prog:
            print("\nOpening Osu!")
            talk("Opening Osu!")
            subprocess.Popen("C:\\Users\\e x a i d e n\\AppData\\Local\\osu!\\osu!.exe")
        elif "mega" in prog:
            print("\nOpening MegaSync")
            talk("Opening Mega sync!")
            subprocess.Popen(
                "C:\\Users\\e x a i d e n\\AppData\\Local\\MEGAsync\\MEGAsync.exe"
            )
        elif "music player" in prog:
            print("\nOpening Music")
            talk("Opening Music")
            system("python Trash_player.py")

        else:
            print("\nTry Again")
            talk("Try Again")

    else:
        talk("Please say the command again.")


while True:
    run_alexa()
