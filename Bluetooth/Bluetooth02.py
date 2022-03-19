import bluetooth
from os import system

system("cls")  # Change 'cls' for 'clear' for Linux or MacOS

system("mode 60,20")
print("---------------[ BLUETOOTH DEVICES SCANNER ]---------------")
while True:
    devices = bluetooth.discover_devices(lookup_names=True)
    for addr, name in devices:
        print("[+] NEW DEVICE:")
        print(f"name: {name}")
        print(f"addr: {addr}")
        print("\n")
    print("------------------------[ NEW SCAN ]------------------------")
    break
