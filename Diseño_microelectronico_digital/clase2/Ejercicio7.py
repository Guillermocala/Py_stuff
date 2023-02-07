# Escriba un programa que lea enteros del usuario y los almacene en
# una lista. Su programa debe continuar leyendo valores hasta que el
# usuario ingrese 0. Luego, debe mostrar todos los valores ingresados
# por el usuario (excepto el 0) en orden de menor a mayor.

def main():
    print("\t\tPedir numeros hasta ingresar 0")
    numeros = []
    while True:
        numero = int(input("Ingrese el numero: "))
        if numero == 0:
            break
        else:
            numeros.append(numero)
    numeros.sort()
    print(numeros)


if __name__ == "__main__":
    main()