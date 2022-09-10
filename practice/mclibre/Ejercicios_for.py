"""     Ejercicio 1: pares e impares en rango"""
rango_inicial = int(input("Ingrese el valor inicial: "))
rango_final = int(input("Ingrese el valor final: "))
for x in range(rango_inicial, (rango_final + 1)):
    if(x % 2 == 0):
        print(x, " es par")
    else:
        print(x, " es impar")
