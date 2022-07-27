import random
"""     Ejercicio 1: azar del 1 al 6
activador = True
while activador:
    print("El numero es: ", random.randint(1, 6))
    keep = input("Si desea terminar el programa pulse intro...")
    if not keep:
        activador = False
"""

"""     Ejercicio 2: azar del 1 al 6 con suma acumulativa
activador = True
suma = 0
while activador:
    numero = random.randint(1, 6)
    suma += numero
    print("El numero es: ", numero, "\nLa suma es: ", suma)
    keep = input("Si desea terminar el programa pulse intro...")
    if not keep:
        activador = False
"""

"""     Ejercicio 3: azar del 1 al 6 con 2 jugadores"""
activador = True
while activador:
    jugador1 = random.randint(1, 6)
    jugador2 = random.randint(1, 6)
    print("Jugador 1: ", jugador1, "\nJugador 2: ", jugador2)
    if jugador1 > jugador2:
        print("Gana jugador 1")
    elif jugador2 > jugador1:
        print("Gana jugador 2")
    else:
        print("Empatados")
    #se puede simplificar la anidación de los 3 casos de la siguiente forma
    #print("Gana jugador 1" if jugador1 > jugador2 else "Gana jugador 2" if jugador2 > jugador1 else "Empate")
    keep = input("Si desea terminar el programa pulse intro...")
    if not keep:
        activador = False