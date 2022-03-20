"""     Ejercicio 1: crear listas"""
def crear_lista(cantidad):
    lista = []
    for item in range(cantidad):
        ingresa = input(f"Ingresa la cantidad {item}: ")
        lista.append(ingresa)
    return lista
numero = int(input("Ingresa el numero de datos: "))
lista = crear_lista(numero)

"""     Ejercicio 2: repetidos
def repetidos(lista, palabra):
    cantidad = 0
    for item in lista:
        if item == palabra:
            cantidad += 1
    return cantidad

def repetidos2(lista, palabra):
    cantidad = lista.count(palabra)
    return cantidad

palabra = input("Ingrese la palabra a buscar: ")
cantidad = repetidos2(lista, palabra)
print(f"la palabra {palabra} fue encontrada {cantidad} veces.")
"""

"""     Ejercicio 3: modificar lista
def reemplazar_item(lista, item1, item2):
    for item in range(len(lista)):
        if lista[item] == item1:
            lista[item] = item2
            return "Reemplazado exitosamente"
    return "No encontrado"

palabra1 = input("Ingrese la palabra a reemplazar: ")
palabra2 = input("Ingrese la palabra de reemplazo: ")
print(reemplazar_item(lista, palabra1, palabra2))
print(lista)
"""

"""     Ejercicio 4: elimina palabra
def elimina_item(lista, item):
    if lista.count(item) == 0:
        return "no encontrado"
    else:
        lista.remove(item)
        return "eliminado exitosamente"

eliminado = input("Ingresa el item a eliminar: ")
print(elimina_item(lista, eliminado))
print(lista)
"""

"""     Ejercicio 5: diferencia listas"""
def diferencia_listas(lista1, lista2):
    lista_temp = lista1.copy()
    for item in lista1:
        if item in lista2:
            lista_temp.remove(item)
    return lista_temp

numero = int(input("2 - Ingresa el numero de datos: "))
lista2 = crear_lista(numero)
listar = diferencia_listas(lista, lista2)
print(listar)
