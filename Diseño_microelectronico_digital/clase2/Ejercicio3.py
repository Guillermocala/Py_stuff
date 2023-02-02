# Escriba un programa que lea un número entero ingresado por el
# usuario. Y luego, muestre un mensaje que indique si el número
# entero es par o impar.

def main():
    print("\t\tNumero par o impar")
    numero = int(input("Ingrese un numero entero: "))
    print("Es par" if numero % 2 == 0 else "Es impar")

if __name__ == "__main__":
    main()