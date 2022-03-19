estudiante1 = {"Nombre": "Elma", "Apellido": "Montt", "Edad": "21", "Grupo": "c2"}

estudiante2 = {"Nombre": "Elsa", "Apellido": "Cowea", "Edad": "21", "Grupo": "c2"}

estudiante3 = {"Nombre": "Elpin", "Apellido": "Chewei", "Edad": "19", "Grupo": "a3"}

estudiante4 = {"Nombre": "Rosa", "Apellido": "Melo", "Edad": "18", "Grupo": "c1"}

estudiante5 = {"Nombre": "Estela", "Apellido": "Prieto", "Edad": "19", "Grupo": "a3"}

estudiante6 = {"Nombre": "Elver", "Apellido": "Galinda", "Edad": "21", "Grupo": "a2"}

estudiante7 = {"Nombre": "Aquiles", "Apellido": "Castro", "Edad": "20", "Grupo": "b2"}

estudiante8 = {"Nombre": "Debora", "Apellido": "Cabezas", "Edad": "22", "Grupo": "b1"}

estudiantes = []
estudiantes.append(estudiante1)
estudiantes.append(estudiante2)
estudiantes.append(estudiante3)
estudiantes.append(estudiante4)
estudiantes.append(estudiante5)
estudiantes.append(estudiante6)
estudiantes.append(estudiante7)
estudiantes.append(estudiante8)

print("Lista de estudiantes:", "\n")
print("", "\n")

print("Estudiante 1: ")
for clave, valor in estudiante1.items():
    print("   ", clave, ":", valor)

print("", "\n")
print("Estudiante 2:")
for clave, valor in estudiante2.items():
    print("   ", clave, ":", valor)

print("", "\n")
print("Estudiante 3: ")
for clave, valor in estudiante3.items():
    print("   ", clave, ":", valor)

print("", "\n")
print("Estudiante 4:")
for clave, valor in estudiante4.items():
    print("   ", clave, ":", valor)

print("", "\n")
print("Estudiante 5: ")
for clave, valor in estudiante5.items():
    print("   ", clave, ":", valor)

print("", "\n")
print("Estudiante 6:")
for clave, valor in estudiante6.items():
    print("   ", clave, ":", valor)

print("", "\n")
print("Estudiante 7: ")
for clave, valor in estudiante7.items():
    print("   ", clave, ":", valor)

print("", "\n")
print("Estudiante 8:")
for clave, valor in estudiante8.items():
    print("   ", clave, ":", valor)

print("", "\n")
