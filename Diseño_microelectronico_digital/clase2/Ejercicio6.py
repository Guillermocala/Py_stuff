# Escriba una función que solicite tres números como parámetros y
# devuelva el valor mediano de los tres.
# Nota: El valor mediano es el medio de los tres valores cuando se
# ordenan en orden ascendente.

def mediano(num1, num2, num3):
    lista = [num1, num2, num3]
    lista.sort()
    return lista[1]

def main():
    print("\t\tNumero mediano")
    num1 = int(input("Ingreses el primer numero: "))
    num2 = int(input("Ingreses el segundo numero: "))
    num3 = int(input("Ingreses el tercero numero: "))
    print("El numero mediano es: ", mediano(num1, num2, num3))

if __name__ == "__main__":
    main()