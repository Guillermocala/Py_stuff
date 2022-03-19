"""     Ejercicio 1: crear listas
def crear_lista(cantidad):
    lista = []
    for item in range(cantidad):
        ingresa = input(f"Ingresa la cantidad {item}: ")
        lista.append(ingresa)
    return lista

numero = int(input("Ingresa el numero de datos: "))
lista = crear_lista(numero)
print(lista)
"""

"""     Ejercicio 2: repetidos
def crear_lista(cantidad):
    lista = []
    for item in range(cantidad):
        ingresa = input(f"Ingresa la cantidad {item}: ")
        lista.append(ingresa)
    return lista

def repetidos(lista, palabra):
    cantidad = 0
    for item in lista:
        if item == palabra:
            cantidad += 1
    return cantidad

numero = int(input("Ingresa el numero de datos: "))
lista = crear_lista(numero)
palabra = input("Ingrese la palabra a buscar: ")
cantidad = repetidos(lista, palabra)
print(f"la palabra {palabra} fue encontrada {cantidad} veces.")
"""

"""     Ejercicio 3: modificar lista
def crear_lista(cantidad):
    lista = []
    for item in range(cantidad):
        ingresa = input(f"Ingresa la cantidad {item}: ")
        lista.append(ingresa)
    return lista

def reemplazar_item(lista, item1, item2):
    for item in range(len(lista)):
        if lista[item] == item1:
            lista[item] = item2
            return "Reemplazado exitosamente"
    return "No encontrado"

numero = int(input("Ingresa el numero de datos: "))
lista = crear_lista(numero)
palabra = input("Ingrese la palabra a reemplazar: ")
palabra2 = input("Ingrese la palabra de reemplazo: ")
print(reemplazar_item(lista, palabra, palabra2))
print(lista)
"""