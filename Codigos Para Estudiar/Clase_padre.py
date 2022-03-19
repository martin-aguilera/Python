class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}"


class Coche(Vehiculo):
    def __init__(self, nombre, edad, velocidad):
        super().__init__(nombre, edad)
        self.velocidad = velocidad

    def __str__(self):
        return f"{super().__str__()}, Velocidad: {self.velocidad}(km/hr)"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo}"


vehiculo = Vehiculo("Negro", 5)
coche = Coche("Blanco", 5, 180)
bicicleta = Bicicleta("Roja", 3, "BMX")

print(vehiculo)
print(coche)
print(bicicleta)
