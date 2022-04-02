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
