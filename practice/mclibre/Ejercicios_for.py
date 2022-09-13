"""     Ejercicio 1: pares e impares en rango
rango_inicial = int(input("Ingrese el valor inicial: "))
rango_final = int(input("Ingrese el valor final: "))
for x in range(rango_inicial, (rango_final + 1)):
    if(x % 2 == 0):
        print(x, " es par")
    else:
        print(x, " es impar")
"""

"""     Ejercicio 2: divisores de un numero"""
numero = int(input("Ingrese un numero mayor que cero: "))
while numero <= 0:
    print("Error")
    numero = int(input("Ingrese un numero mayor que cero: "))
else:
    print("Divisores: ")
    for x in range(1, (numero + 1)):
        if numero % x == 0:
            print(x, end=", ")

