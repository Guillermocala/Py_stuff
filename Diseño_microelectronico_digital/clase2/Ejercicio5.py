# Escrita un programa que de cómo resultado un archivo de texto con
# una matriz que muestre todas las combinaciones de multiplicación de
# los número 1 hasta 10.

def main():
    print("\t\tTablas de multiplicar")
    res = ""
    for x in range(1, 10):
        for y in range(10):
            res += str(x) + " x " + str(y) + " = " + str(x * y) + "\n"
        res += "\n"
    with open('tablas_multiplicar.txt', 'w') as f:
        f.write(res)
        print("txt generado exitosamente!")

if __name__ == "__main__":
    main()