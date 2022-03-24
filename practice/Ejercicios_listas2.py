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

"""     Ejercicio 3: num primos
def primos(numero):
    lista = []
    for i in range(1, numero + 1):
        cant = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cant += 1
        if cant == 2:
            lista.append(i)
    return lista

numero = int(input("Ingrese el numero: "))
print(f"Primos hasta {numero} : ", primos(numero))
"""

"""     Ejercicio 4: sucesión 1
def sucesion1(a, b, u, cantidad):
    lista = [u]
    for i in range(cantidad):
        res = a * lista[len(lista) - 1] + b
        lista.append(res)
    return lista

print("Cálculo de términos de una sucesión U(n+1)=a.U(n)+b.")
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
u = int(input("Ingrese el valor de U(0): "))
cant = int(input("Digame cuantos términos quiere: "))
print("Los términos de la sucesión son: ", sucesion1(a, b, u, cant))
"""

"""     Ejercicio 5: sucesión 2
def sucesion2(u, cantidad):
    lista = [u]
    for i in range(cantidad - 1):
        ultimo_item = lista[len(lista) - 1]
        if ultimo_item % 2 == 0:
            res = ultimo_item // 2
            lista.append(res)
        else:
            res = 3 * ultimo_item + 1
            lista.append(res)
    return lista

print("Cálculo de términos de la sucesión U(n+1)=3.U(n)+1 si n es impar y U(n)=U(n)/2 si n es par.")
u = int(input("Ingrese el valor de U(0): "))
cant = int(input("Digame cuantos términos quiere: "))
print("Los términos de la sucesión son: ", sucesion2(u, cant))
"""