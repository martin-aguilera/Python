import os
from getpass import getpass
from tabulate import tabulate
from Conexion import *
import Usuario
import Contraseña

conexion = conectar()
crear_tablas(conexion)


def inicio():
    os.system("cls")
    comprobar = Usuario.comprobar_usuario()
    if len(comprobar) == 0:
        print("Bienvenido, registre su informacion")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
        respuesta = Usuario.registrar(nombre, apellido, contrasena_maestra)
        if respuesta == "Registro correcto":
            print(f"Bienvenido {nombre}")
            menu()
        else:
            print(respuesta)
    else:
        contrasena_maestra = getpass("Ingrese su contraseña maestra: ", "\n")
        respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
        if len(respuesta) == 0:
            print("Contraseña incorrecta")
        else:
            print("Bienvenido", "\n")
            menu()


def menu():
    while True:
        print("Seleccione una de las siguientes opciones: ")
        print("\t1 Añadir contraseña")
        print("\t2 Ver todas las contraseñas")
        print("\t3 Ver solo una contraseña")
        print("\t4 Modificar contraseña")
        print("\t5 Eliminar contraseña")
        print("\t6 Salir")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            nueva_contrasena()

        elif opcion == "2":
            mostrar_contrasenas()

        elif opcion == "3":
            buscar_contrasenas()

        elif opcion == "4":
            modificar_contrasena()

        elif opcion == "5":
            eliminar_contrasena()

        elif opcion == "6":
            break

        else:
            print("\tNo ingreso una opcion valida")


def nueva_contrasena():
    nombre = input("Ingresa el nombre: ")
    url = input("Ingrese la url: ")
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    descripcion = input("Ingrese la descripcion: ")
    respuesta = Contraseña.registrar(
        nombre, url, nombre_usuario, contrasena, descripcion
    )
    print(respuesta)


def mostrar_contrasenas():
    datos = Contraseña.mostrar()
    nuevos_datos = []
    headers = ["ID", "NOMBRE", "URL", "USUARIO", "CONTRASEÑA", "DESCRIPCIÓN"]
    for dato in datos:
        convertido = list(dato)
        convertido[4] = "********"
        nuevos_datos.append(convertido)
    tabla = tabulate(nuevos_datos, headers, tablefmt="fancy_grid")
    print("\t\t\t\tTodas las contraseñas")
    print(tabla)


def buscar_contrasenas():
    contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if (len(respuesta)) == 0:
        print("Contraseña Incorrecta")
    else:
        id = input("Ingrese el id de la contraseña a buscar: ")
        datos = Contraseña.buscar(id)
        headers = ["ID", "NOMBRE", "URL", "USUARIO", "CONTRASEÑA", "DESCRIPCIÓN"]
        tabla = tabulate(datos, headers, tablefmt="fancy_grid")
        print("\t\t\t\tTodas las contraseñas")
        print(tabla)


def modificar_contrasena():
    contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if (len(respuesta)) == 0:
        print("Contraseña Incorrecta")
    else:
        id = input("Ingrese el id a modificar: ")
        nombre = input("Ingrese el nuevo nombre: ")
        url = input("Ingrese la nueva url: ")
        nombre_usuario = input("Ingrese el nuevo nombre de usuario: ")
        contrasena = input("Ingrese la nueva contraseña: ")
        descripcion = input("Ingrese la nueva descripcion: ")
        respuesta = Contraseña.modificar(
            id, nombre, url, nombre_usuario, contrasena, descripcion
        )
        print(respuesta)


def eliminar_contrasena():
    contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if (len(respuesta)) == 0:
        print("Contraseña Incorrecta")
    else:
        id = input("Ingrese el id de la contraseña a eliminar: ")
        respuesta = Contraseña.eliminar(id)
        print(respuesta)


inicio()
