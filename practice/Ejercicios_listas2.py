"""def crear_lista(cantidad):
    lista = []
    for item in range(cantidad):
        ingresa = input(f"Ingresa la cantidad {item}: ")
        lista.append(ingresa)
    return lista
numero = int(input("Ingresa el numero de datos: "))
lista = crear_lista(numero)"""

"""     Ejercicio 1: orden alfabetico(algoritmo de ordenamiento)
def orden_alfabetico(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[menor] > lista[j]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

print(orden_alfabetico(lista))
"""

"""     Ejercicio 2: divisores de un numero
def divisores(numero):
    lista = []
    for item in range(1, numero + 1):
        if numero % item == 0:
            lista.append(item)
    return lista

numero = int(input("Ingrese el numero: "))
print(f"{numero} tiene los sgtes divisores: ", divisores(numero))
"""

"""     Ejercicio 3: num primos"""
def primos(numero):
    lista = []
    for i in range(1, numero + 1):
        cont = 0
        for j in range(i, numero + 1):
            if numero % j == 0:
                cont += 1
                if cont == 2:
                    lista.append(i)
                    cont = 0
    return lista

numero = int(input("Ingrese el numero: "))
print(f"Primos hasta {numero} : ", primos(numero))