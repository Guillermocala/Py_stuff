"""     Ejercicio 1: pedir 2do mientras sea menor
def numero_mayor(num1, num2):
    while num1 >= num2:
        num2 = int(input(f"{num2} no es mayor que {num1}. Intentelo de nuevo: "))
    print(f"Los numeros que ha escrito son {num1} y {num2}")

num1 = int(input("Escriba un numero: "))
num2 = int(input(f"Escriba un numero mayor que {num1}: "))
numero_mayor(num1, num2)
"""

"""     Ejercicio 2: numeros mayores
def numeros_mayores(num1, num2):
    while num1 <= num2:
        num2 = float(input(f"Escriba otro numero mayor que {num1}: "))
    print(f"{num2} no es mayor que {num1}")

num1 = float(input("Escriba un numero: "))
num2 = float(input(f"Escriba un numero mayor que {num1}: "))
numeros_mayores(num1, num2)
"""

"""     Ejercicio 3: cada vez mas grandes
def mas_grandes(num1, num2):
    while num1 < num2:
        num1 = num2
        num2 = int(input(f"Escriba un numero mayor que {num1}: "))
    print(f"{num2} no es mayor que {num1}")

num1 = int(input("Escriba un numero: "))
num2 = int(input(f"Escriba un numero mayor que {num1}: "))
mas_grandes(num1, num2)
"""

"""     Ejercicio 4: numeros positivos
def numeros_positivos(cant_numeros):
    cant_positivos = 0
    for item in range(cant_numeros):
        numero = int(input("Escriba el numero: "))
        if numero > 0:
            cant_positivos += 1
    print(f"Ha escrito {cant_numeros} numeros, {cant_positivos} de ellos positivos")
            
cant = int(input("Escriba la cantidad de numeros positivos a escribir: "))
while cant < 1:
    cant = int(input("La cantidad debe ser mayor a 0. Intente de nuevo: "))
numeros_positivos(cant)
"""

"""     Ejercicio 5: suma de numeros
def suma_numeros(numero):
    suma = 0
    while numero > 0:
        suma += numero
        numero = int(input("Ingrese otro numero: "))
    else:
        print(f"La suma de los numeros positivos ingresados es {suma}")

num = int(input("Ingrese un numero: "))
suma_numeros(num)
"""

"""     Ejercicio 6: limite positivo
def limite_positivo(limite):
    while limite < 1:
        limite = int(input("el limite debe ser mayor a 0. Intente de nuevo: "))
    else:
        suma = limite
        num = 0
        while num < suma:
            num += int(input("Escriba un numero: "))
        else:
            print(f"Ha superado el limite. La suma de los ingresados es: {num}")

numero = int(input("Escriba el valor del limite: "))
limite_positivo(numero)
"""

"""     Ejercicio 7: intervalo
def intervalo(min, max):
    numero = float(input("Ingrese un numero: "))
    cant = 0
    while numero < max and numero > min:
        cant += 1
        numero = float(input("Ingrese otro numero: "))
    else:
        print(f"Ha escrito {cant} numeros entre {min} y {max}")

num_min = int(input("Ingrese el invervalo 1: "))
while num_min < 1:
    num_min = int(input("el limite debe ser mayor a 0. Intente de nuevo: "))
num_max = int(input("Ingrese el invervalo 2: "))
while num_max <= num_min:
    num_max = int(input("el limite debe ser mayor al limite 1. Intente de nuevo: "))
intervalo(num_min, num_max)
"""

"""     Ejercicio 8: pedir pares
def pide_pares():
    cant = 0
    while True:
        numero = int(input("Escriba un numero: "))
        while numero % 2 != 0:
            numero = int(input(f"{numero} no es un numero par. Intente de nuevo: "))
        else: 
            cant += 1
        opcion = input("Quiere ingresar otro numero par? (S/N): ")
        if opcion not in "sS":
            break
    print(f"Ha escrito {cant} numero par")

pide_pares()
"""

"""     Ejercicio 8.2: mejora
def pide_pares():
    cant = 0
    while True:
        numero = int(input("Escriba un numero: "))
        while numero % 2 != 0:
            numero = int(input(f"{numero} no es un numero par. Intente de nuevo: "))
        else: 
            cant += 1
        opcion = input("Quiere ingresar otro numero par? (S/N): ")
        while opcion not in "sSnN":
            opcion = input("Quiere ingresar otro numero par? (S/N): ")
        if opcion in "nN":
            break
    print(f"Ha escrito {cant} numero par")

pide_pares()
"""

"""     Ejercicio 9: descomposicion factores primos"""
def descomposicion_factorial(numero):
    copia = numero
    while copia > 1:
        for i in range(2, copia + 1):
            if copia % i == 0:
                print(copia, "\t", i)
                copia //= i     #equals to copia = copia // i
                break
    print(copia)

print("DESCOMPOSICIÓN FACTORES PRIMOS")
numero = int(input("Escriba un numero entero mayor que 1: ")) 
while numero < 2:
    numero = int(input(f"{numero} no es mayor que 1. Intentelo de nuevo: "))
descomposicion_factorial(numero)