# Escriba un programa que cree dos archivos en formato txt: el primero
# debe imprimir los números enteros desde 0 hasta 100, el segundo
# debe imprimir los números enteros desde 50 hasta 200. Luego
# escriba otro programa que lea ambos archivos y genere un archivo
# nuevo que contenga sólo números pares organizados de mayor a
# menor, estos números no deben estar repetidos.

def main():
    print("\t\tGenerador de numeros(PARTE B)")
    res = ""
    archivo1 = open("numeros_0_a_100.txt", "r")
    archivo2 = open("numeros_50_a_200.txt", "r")
    archivo_final = open("pares_ordenados_descendente.txt", "w")
    # comprehension de listas para extraer de los archivos txt
    lista_0_a_100 = [int(x) for x in archivo1.readlines()]
    lista_50_a_200 = [int(x) for x in archivo2.readlines()]
    # combinamos las listas bajo un set para quitar repetidos
    lista_combinada = set(lista_0_a_100 + lista_50_a_200)
    # comprehension de listas para quedarnos con los pares
    lista_pares = [x for x in lista_combinada if x % 2 == 0]
    # metodo sort para dejar en forma descendente
    lista_pares.sort(reverse=True)
    # solo concatenamos y escribimos en el txt
    for i in lista_pares:
        res += str(i) + "\n"
    archivo_final.write(res)

    print("Archivo generado exitosamente!")

if __name__ == "__main__":
    main()