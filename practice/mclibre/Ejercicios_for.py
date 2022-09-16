"""     Ejercicio 1: pares e impares en rango
rango_inicial = int(input("Ingrese el valor inicial: "))
rango_final = int(input("Ingrese el valor final: "))
for x in range(rango_inicial, (rango_final + 1)):
    if(x % 2 == 0):
        print(x, " es par")
    else:
        print(x, " es impar")
"""

"""     Ejercicio 2: divisores de un numero
numero = int(input("Ingrese un numero mayor que cero: "))
while numero <= 0:
    pri("Error")
    numero = int(input("Ingrese un numero mayor que cero: "))
else:
    print("Divisores: ")
    for x in range(1, (numero + 1)):
        if numero % x == 0:
            print(x, end=", ")
"""

"""     Ejercicio 3: mayor al primero
primer_numero = 0
numero = int(input("Ingrese la cantidad de datos: "))
for x in range(0, numero):
    numero_actual = int(input("Ingrese un numero: "))
    if x == 0:
        primer_numero = numero_actual
    if primer_numero > numero_actual:
        print("El numero es menor que el primer numero")
"""

"""     Ejercicio 4: mayor al ultimo
numero_anterior = 0
numero = int(input("Ingrese la cantidad de datos: "))
for x in range(0, numero):
    numero_actual = int(input("Ingrese un numero: "))
    if numero_anterior > numero_actual:
        print("El numero es menor que el anterior")
    numero_anterior = numero_actual
"""


"""     Ejercicio 5: identificador numeros negativos"""
cantidad_negativos = 0
numero = int(input("Ingrese la cantidad de datos: "))
for x in range(numero):
    numero_actual = int(input("Ingrese un numero: "))
    if numero_actual < 0:
        cantidad_negativos += 1
print("La cantidad de negativos es: ", cantidad_negativos)

