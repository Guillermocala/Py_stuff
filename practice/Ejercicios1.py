"""     Ejercicio 1- Funcion max()
def max(num1, num2):
    return (num1 if num1 > num2 else num2)

num1 = int(input("ingresa num1: "))
num2 = int(input("ingresa num2: "))
print("el mayor es: " , max(num1, num2))
"""

"""     Ejercicio 2- max_de_tres()
def max_de_tres(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

num1 = int(input("ingresa num1: "))
num2 = int(input("ingresa num2: "))
num3 = int(input("ingresa num3: "))
print("el mayor es: " , max_de_tres(num1, num2, num3))
"""

"""     Ejercicio 3- funcion length()
def length(cadena):
    contador = 0
    for item in cadena:
        contador += 1
    return contador

nombre = input("Ingresa tu nombre: ")
print("Tu nombre tiene: ", length(nombre), " caracteres")
lista = [0, 1, 2, 3, 4, 5]
print(lista)
print("La lista tiene: ", length(lista), " elementos")
"""

"""     Ejercicio 4- es_vocal()
def es_vocal(caracter):
    return (True if caracter in "aeiouAEIOU" else False)
    
caracter = input("Ingresa un caracter: ")
print("El caracter es vocal? :  ", es_vocal(caracter))
"""

"""     Ejercicio 5- suma() | multiplicacion()
def suma(lista):
    sumatoria = 0
    for item in lista:
        sumatoria += item
    return sumatoria

def multiplicacion(lista):
    producto = 1
    for item in lista:
        producto *= item
    return producto

lista = [2, 5, 3, 4]
print(lista)
print("La sumatoria es: ", suma(lista))
print("La producto es: ", multiplicacion(lista))
"""

"""     Ejercicio 6- inversa()
def inversa(cadena):
    respuesta = ""
    length = len(cadena)
    for item in range(length):
        respuesta += cadena[length - 1]
        length -= 1
    return respuesta

palabra = input("ingresa una palabra: ")
print("La inversa es: ", inversa(palabra))
"""

"""     Ejercicio 7- es_palindromo()
def inversa(cadena):
    respuesta = ""
    length = len(cadena)
    for item in range(length):
        respuesta += cadena[length - 1]
        length -= 1
    return respuesta

def es_palindromo(palabra):
    palabra_invertida = inversa(palabra)
    if palabra == palabra_invertida:
        return True
    else:
        return False

palabra = input("Ingresa una palabra: ")
if es_palindromo(palabra):
    print("La palabra es palindroma")
else:
    print("La palabra no es palindroma")
"""

"""     Ejercicio 8- superposicion()
def superposicion(lista1, lista2):
    for item in lista1:
        if item in lista2:
            return True
    else:
        return False

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8]
print(superposicion(lista2, lista1))
"""

"""     Ejercicio 9- generar_n_caracteres()
def generar_n_caracteres(num, caracter):
    return (caracter * num)

caracter = input("ingresa un caracter: ")
veces = int(input("ingresa un numero: "))
print(generar_n_caracteres(caracter, veces))
"""

"""     Ejercicio 10- histograma()
def histograma(lista):
    for item in lista:
        print("*" * item)

lista = [1, 5, 3, 2, 6]
histograma(lista)
"""