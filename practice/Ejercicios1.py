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