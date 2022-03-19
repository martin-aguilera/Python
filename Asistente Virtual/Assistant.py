import speech_recognition as sr
import pyttsx3, pywhatkit, urllib.request, json, datetime, pyjokes, wikipedia, subprocess, pyautogui  # bluetooth,
from os import system
from joke_generator import generate
from random import choice

system("cls")

jokes = [pyjokes.get_joke(), generate()]
key = "AIzaSyCYEQsjqR1Y0V9KhVgNP7uiCegeAdhYFsw"
name = "aliz"
listener = sr.Recognizer()
engine = pyttsx3.init()
voice_spd = 190
voices = engine.getProperty("voices")

engine.setProperty("rate", voice_spd)
engine.setProperty("voice", voices[2].id)  # change the assistant's voice.


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


def listen_main():
    try:
        with sr.Microphone() as source:
            print("hi!, ¿what do you need?\n")
            talk("hi!, ¿what do you need?")
            print("\nListening...\n")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            print(rec)
    except:
        print("I can't hear you\n")
    return rec


while True:

    def run():
        rec = listen_main()
        system("cls")

        if "introduce yourself" in rec:
            print("\nHi there!, my name is " + name)
            talk("Hi there!, my name is " + name)
            print("I am a virtual assistant that has not been finished yet")
            talk("I am a virtual assistant that has not been finished yet")
            print("I hope i can be usefull someday")
            talk("I hope i can be usefull someday")

        elif "your name" in rec:
            print("\nMy name is " + name + ", try not to forget it pls")
            talk("\nMy name is " + name + ", try not to forget it please")

        elif "open" in rec:
            prog = rec.replace("open", "")
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
                subprocess.Popen(
                    "C:\\Users\\e x a i d e n\\Desktop\\Desktop 2\\Archivos\\osu!\\osu!.exe"
                )
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

        elif "play on youtube" in rec:
            music = rec.replace("play on youtube", "")
            print("\nPlaying " + music)
            talk("Playing " + music)
            pywhatkit.playonyt(music)

        elif "what time is" in rec:
            hora = datetime.datetime.now().strftime("%I:%M %p")
            print("\nIt is " + hora)
            talk("it is " + hora)

        elif "search for" in rec:
            order = rec.replace("search for", "")
            info = wikipedia.summary(order, 1)
            print("\n", info)
            talk(info)

        elif "joke" in rec or "something funny" in rec:
            joke = choice(jokes)
            print("\n", joke)
            talk(joke)

        elif "let's play" in rec or "lets play" in rec:
            play = rec.replace("let's play", "")
            if "snake" in play:
                print(f"\nOk, but let me play {play} after you.")
                talk(f"Ok, but let me play {play} after you.")
                system("python games/Snake_pygame.pyw")
            elif "ping pong" in play:
                print(f"\nOk, but let me play {play} with you someday.")
                talk(f"Ok, but let me play {play} with you someday.")
                system("python games/Pong_pygame.pyw")

        elif "screenshot" in rec:
            screenshot = pyautogui.screenshot()
            print("Taking an screenshot")
            talk("Taking an screenshot")
            screenshot.save("output/shot.jpg")

        elif "how many subscribers has" in rec:
            name_subs = rec.replace("how many subscribers has", "").strip()
            data = urllib.request.urlopen(
                "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="
                + name_subs
                + "&key="
                + key
            ).read()
            subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
            print(name_subs + " has {:,d}".format(int(subs)) + " subscribers!")
            talk(name_subs + " has {:,d}".format(int(subs)) + " subscribers!")
            # print('\nAnd why the fuck do you think I know that? Move your lazy ass and go see it yourself')
            # talk('And why the fuck do you think I know that? Move your lazy ass and go see it yourself')

        elif "show me all saved wi-fi" in rec or "show me all saved wifi" in rec:
            print("\nOk, just wait for a sec...")
            talk("Ok, just wait for a second")
            print("\n*******************************************************")
            system("netsh wlan show profiles")

        elif "export wifi data" in rec or "export wi-fi data" in rec:
            print("\nOk, just wait for a sec...")
            talk("Ok, just wait for a second")
            system("netsh wlan export profile folder=C:\ key=clear")

        # elif 'search bluetooth' in rec:
        # print('\nScanning, just wait for a sec...')
        # talk('Scanning, just wait for a second...')
        # Bluetooth()

        elif "nothing" in rec:
            print("\nOh!, ok. bye bye")
            talk("oh!, ok. bye bye")

        else:
            print("\nPlease, try again")
            talk("Please, try again")

    run()
    break
