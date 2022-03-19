import bluetooth
from os import system

system("cls")  # Change 'cls' for 'clear' for Linux or MacOS

print("\nWait a sec...")
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("\n\nFound %d devices" % len(nearby_devices), "\n")

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name), "\n")
