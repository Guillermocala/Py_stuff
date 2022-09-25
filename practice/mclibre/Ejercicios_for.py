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


"""     Ejercicio 5: identificador numeros negativos
cantidad_negativos = 0
numero = int(input("Ingrese la cantidad de datos: "))
for x in range(numero):
    numero_actual = int(input("Ingrese un numero: "))
    if numero_actual < 0:
        cantidad_negativos += 1
print("La cantidad de negativos es: ", cantidad_negativos)
"""

"""     Ejercicio 6: contador pares e impares
cantidad_pares = 0
cantidad_impares = 0
numero = int(input("Ingrese la cantidad de datos: "))
for x in range(numero):
    numero_actual = int(input("Ingrese un numero: "))
    if numero_actual % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1
print("La cantidad de pares es: ", cantidad_pares)
print("La cantidad de impares es: ", cantidad_impares)
"""


"""     Ejercicio 7: numero primo 
divisores = 1
print("verificador numeros primos, debe ingresar un numero mayora a 1")
numero = int(input("Ingrese el numero: "))
for x in range(1, numero):
    if numero % x == 0:
        divisores += 1
if divisores == 2:
    print("Es primo")
else:
    print("No es primo")
"""

"""     Ejercicio 8: suma numeros
suma = 0
numero = int(input("Cantidad de numeros: "))
for x in range(numero):
    aux = float(input("ingrese un numero: "))
    suma += aux
print("La suma es: ", suma)
"""

"""     Ejercicio 9: suma en rango
suma = 0
print("Suma de numeros en rango, debe insertar el numero inicial y final...")
numero_inicial = int(input("Ingrese el numero inicial: "))
numero_final = int(input("Ingrese el numero final: "))
while numero_final <= numero_inicial:
    print("El numero final no puede ser menor o igual al inicial!")
    numero_final = int(input("Ingrese el numero final: "))
for x in range(numero_inicial, (numero_final + 1)):
    suma += x
print("La suma es: ", suma)
"""

"""     Ejercicio 10: suma en rango con sumandos en pantalla 
suma = 0
print("Suma de numeros en rango, debe insertar el numero inicial y final...")
numero_inicial = int(input("Ingrese el numero inicial: "))
numero_final = int(input("Ingrese el numero final: "))
while numero_final <= numero_inicial:
    print("El numero final no puede ser menor o igual al inicial!")
    numero_final = int(input("Ingrese el numero final: "))
for x in range(numero_inicial, (numero_final + 1)):
    suma += x
    if x != numero_final:
        print(x, end=" + ")
    else:
        print(x, end=" = ")
print(suma)
"""

'''     Ejercicio 11: mayor, menor y media de n numeros
suma = 0
mayor = 0;
menor = 99999;
print("Mayor, menor y media de numeros")
cantidad = int(input("Ingrese la cantidad de numeros: "))
for x in range(cantidad):
    numero = int(input("Ingrese el numero: "))
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    suma += numero
media = suma / cantidad
print(f"""
            Estadisticas
        El numero mayor es: {mayor} 
        El numero menro es: {menor} 
        La media es: {media}
        """)
'''

"""     Ejercicio 12: calcular factorial """
factorial = 1
numero = int(input("Ingrese el numero mayor a cero: "))
while numero < 1:
    print("el numero debe ser mayor a cero!")
    numero = int(input("Ingrese el numero mayor a cero: "))
for x in range(1, (numero + 1)):
    factorial *= x
print("El factorial es: ", factorial)
