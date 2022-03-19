try:
    archivo = open("prueba.txt", "w", encoding="utf8")
    archivo.write("Pico pal ke lee\n")
    archivo.write("      xdd")
except Exception as e:
    print(e)
finally:
    archivo.close()
    print("\n F I N")
