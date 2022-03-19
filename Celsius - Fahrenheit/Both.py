def celsius_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    print(str(celsius) + "°C = " + str(fahrenheit) + "°F")


def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    print(str(fahrenheit) + "°F = " + str(celsius) + "°C")


celsius = float(input("Ingresa °C: "))
resultado = celsius_fahrenheit(celsius)
fahrenheit = float(input("Ingresa °F: "))
resultado = fahrenheit_celsius(fahrenheit)
