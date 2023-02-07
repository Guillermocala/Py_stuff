# Escriba un programa que cree dos archivos en formato txt: el primero
# debe imprimir los números enteros desde 0 hasta 100, el segundo
# debe imprimir los números enteros desde 50 hasta 200. Luego
# escriba otro programa que lea ambos archivos y genere un archivo
# nuevo que contenga sólo números pares organizados de mayor a
# menor, estos números no deben estar repetidos.

def main():
    print("\t\tGenerador de numeros(PARTE A)")
    archivo1 = open("numeros_0_a_100.txt", "w")
    archivo2 = open("numeros_50_a_200.txt", "w")
    res1, res2 = "", ""
    for i in range(201):
        if i <= 100:
            res1 += str(i) + "\n"
        if i >= 50:
            res2 += str(i) + "\n"
    archivo1.write(res1)
    archivo2.write(res2)
    print("Archivos generados exitosamente!")

if __name__ == "__main__":
    main()