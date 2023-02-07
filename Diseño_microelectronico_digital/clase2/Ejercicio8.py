# Escriba un programa que lee palabras del usuario hasta que el
# usuario ingresa la palabra fin. Su programa debe mostrar cada
# palabra ingresada por el usuario exactamente una vez.

def main():
    print("\t\tPalabras dadas por el usuario")
    print("\tSe terminara cuando ingrese la palabra: fin")
    palabras = set()
    while True:
        palabra = input("Ingrese una palabra: ")
        if palabra.lower() == "fin":
            break
        else:
            palabras.add(palabra)
    print(palabras)

if __name__ == "__main__":
    main()