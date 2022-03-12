"""     Ejercicio 1: max_in_list()
def max_in_list(lista):
    acumulador = 0
    for item in lista:
        if item > acumulador:
            acumulador = item
    return acumulador

lista = [23, 1, 12, 8, 19]
print("El mayor de la lista es: ", max_in_list(lista))
"""

"""     Ejercicio 2: mas_larga()
def mas_larga(lista):
    acumulador = 0
    palabra_ganadora = ""
    for item in lista:
        if len(item) > acumulador:
            acumulador = len(item)
            palabra_ganadora = item
    return palabra_ganadora

lista = ["Juan", "Hernesto", "Perensejo", "Guillermo"]
print("La palabra mas larga es: ", mas_larga(lista))
"""

"""     Ejercicio 3: filtrar_palabras()
def filtrar_palabras(lista, cantidad):
    resultado = []
    for item in lista:
        if len(item) == cantidad:
            resultado.append(item)
    return resultado

lista = ["Juan", "Hernesto", "Jose", "Toti", "Perensejo", "Guillermo"]
cantidad = int(input("Ingrese el numero de caracteres: "))
print("Las palabras filtradas son: ", filtrar_palabras(lista, cantidad))
"""

"""     Ejercicio 4: letras_mayusculas()
def cantidad_mayusculas(cadena):
    cantidad = 0
    for item in cadena:
        if item.isupper():
            cantidad += 1
    return cantidad

cadena = input("Ingrese una cadena de caracteres que contenga mayusculas: ")
print("La cantidad de mayus es: ", cantidad_mayusculas(cadena))
"""

"""     Ejercicio 5: binario_a_entero()
def binario_a_entero(numero):
    lista = [int(x) for x in str(numero)]
    lista.reverse()
    acumulador = 0
    for item in range(len(lista)):
        if lista[item] == 1:
            acumulador += 2 ** item
    return acumulador

numero_binario = input("Ingrese un numero binario: ")
print("El numero entero es: ", binario_a_entero(numero_binario))
"""

