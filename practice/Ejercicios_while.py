"""     Ejercicio 1: continuar"""
def continuar():
    print("DIGA sí PARA CONTINUAR")
    temp = input("¿Desea continuar el programa?: ")
    while temp == "sí":
        temp = input("¿Desea continuar el programa?: ")
    else: 
        print("¡Hasta la vista!")

continuar()