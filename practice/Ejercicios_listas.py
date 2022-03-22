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

"""     Ejercicio 5: diferencia listas
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
"""

"""     Ejercicio 6: reverse lista
def voltear_lista(lista):
    listar = lista.copy()
    listar.reverse()
    '''otro metodo:
        listar = lista[::-1]
        hace la copia y directamente la pone al reves'''
    return listar

print("lista reverse: ", voltear_lista(lista))
"""

"""     Ejercicio 7: elimina ocurrencias(excepto la primera)
#sacamos el indice de la primera ocurrencia, eliminamos todos y al final
#insertamos el dato en donde estaba su primera ocurrencia
def elimina_ocurrencias(lista, dato):
    if lista.count(dato) != 0:
        position = lista.index(dato)
        while lista.count(dato) != 0:
            lista.remove(dato)
        lista.insert(position, dato)
    else:
        return "dato no encontrado"
    return lista
    
eliminar = input("Ingresa el dato a eliminar: ")
print(elimina_ocurrencias(lista, eliminar))
"""

"""     extra: eliminar repetidos de una lista
def elimina_ocurrencias(lista):
    for item in lista:
        if lista.count(item) > 1:
            position = lista.index(item)
            while lista.count(item) != 0:
                lista.remove(item)
            lista.insert(position, item)
"""

"""     Ejercicio 8: operaciones listas"""
def elimina_ocurrencias(lista):
    for item in lista:
        if lista.count(item) > 1:
            position = lista.index(item)
            while lista.count(item) != 0:
                lista.remove(item)
            lista.insert(position, item)

def estadisticas(lista1, lista2):
    items_ambas_listas = []
    primera_no_segunda = []
    segunda_no_primera = []
    for item in lista1:
        if item in lista2:
            items_ambas_listas.append(item)
        elif item not in lista2:
            primera_no_segunda.append(item)
    for item in lista2:
        if item not in lista1:
            segunda_no_primera.append(item)
    print("Ahora las estadisticas...")
    print("ambas listas: ", items_ambas_listas)
    print("primera no segunda: ", primera_no_segunda)
    print("segunda no primera: ", segunda_no_primera)


numero2 = int(input("Ingresa el numero de datos: "))
lista2 = crear_lista(numero2)
elimina_ocurrencias(lista)
elimina_ocurrencias(lista2)
estadisticas(lista, lista2)

