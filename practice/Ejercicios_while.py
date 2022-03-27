"""     Ejercicio 1: continuar
def continuar():
    print("DIGA sí PARA CONTINUAR")
    temp = input("¿Desea continuar el programa?: ")
    while temp == "sí":
        temp = input("¿Desea continuar el programa?: ")
    print("¡Hasta la vista!")

continuar()
"""

"""     Ejercicio 2: continuar2
def continuar():
    print("DIGA SI PARA CONTINUAR")
    temp = input("¿Desea continuar el programa?: ")
    while temp != "SI":
        temp = input("¿Desea continuar el programa?: ")
    print("¡Hasta la vista!")

continuar()
"""

"""     Ejercicio 3: continuar3
def continuar():
    print("DIGA N PARA CONTINUAR")
    temp = input("¿Desea continuar el programa?: ")
    while temp == "N":
        temp = input("¿Desea continuar el programa?: ")
    print("¡Hasta la vista!")

continuar()
"""

"""     Ejercicio 4: continuar4
def continuar():
    print("DIGA no PARA CONTINUAR")
    temp = input("¿Desea continuar el programa?: ")
    while temp != "no":
        temp = input("¿Desea continuar el programa?: ")
    print("¡Hasta la vista!")

continuar()
"""

"""     Ejercicio 5: continuar5
def continuar():
    print("DIGA S o s PARA CONTINUAR")
    temp = input("¿Desea continuar el programa?: ")
    claves = ["S", "s"]
    while temp in claves:
        temp = input("¿Desea continuar el programa?: ")
    print("¡Hasta la vista!")

continuar()
"""

"""     Ejercicio 6: continuar6
def continuar():
    print("DIGA S o s PARA CONTINUAR")
    temp = input("¿Desea continuar el programa?: ")
    claves = ["S", "s"]
    while temp not in claves:
        temp = input("¿Desea continuar el programa?: ")
    print("¡Hasta la vista!")

continuar()
"""

"""     Ejercicio 7: confirmar contraseña
def confirmar_contra():
    print("CONFIRME SU CONTRASEÑA")
    contra = input("Escriba su contraseña: ")
    contra2= input("Escriba de nuevo su contraseña: ")
    while contra != contra2:
        print("Las contraseñas no coinciden. Inténtelo de nuevo.")
        contra = input("Escriba su contraseña: ")
        contra2= input("Escriba de nuevo su contraseña: ")
    print("Contraseña confirmada ¡Hasta la vista!")

confirmar_contra()
"""

"""     Ejercicio 8: hucha(alcancía)
def hucha():
    print("HUCHA")
    objetivo = int(input("¿Cuántos euros quiere ahorrar?: "))
    acumulador = int(input("¿Cuántos euros quiere meter en la hucha?: "))
    while acumulador < objetivo:
        temp = int(input("¿Cuántos euros quiere meter en la hucha?: "))
        acumulador += temp
    print(f"¡Objetivo conseguido! Ha ahorrado usted {acumulador} euros.")

hucha()
"""

"""     Ejercicio 9: hucha mejorada
def es_negativo(numero):
    return (True if numero < 1 else False)

def hucha_mejorada():
    print("HUCHA MEJORADA")
    hucha = 0
    objetivo = int(input("¿Cuántos euros quiere ahorrar?: "))
    while es_negativo(objetivo):
        print("Ha ingresado un valor invalido!")
        objetivo = int(input("¿Cuántos euros quiere ahorrar?: "))
    while hucha < objetivo:
        ingreso = int(input("¿Cuántos euros quiere meter en la hucha?: "))
        while es_negativo(ingreso):
            print("Ha ingresado un valor invalido!")
            ingreso = int(input("¿Cuántos euros quiere meter en la hucha?: "))
        hucha += ingreso
    print(f"¡Objetivo conseguido! Ha ahorrado usted {hucha} euros.")

hucha_mejorada()
"""

"""     Ejercicio 10: confirmar contraseña 3 intentos"""
def confirmar_contra():
    print("CONFIRME SU CONTRASEÑA (3 intentos)")
    intentos = 3
    contra = input("Escriba su contraseña: ")
    print("Tiene 3 intentos para confirmar su contraseña")
    contra2= input("Escriba de nuevo su contraseña: ")
    while contra != contra2 and intentos > 1:
        print("Las contraseñas no coinciden. Inténtelo de nuevo.")
        contra2= input("Escriba de nuevo su contraseña: ")
        intentos -= 1
    print("Contraseña confirmada ¡Hasta la vista!")

confirmar_contra()