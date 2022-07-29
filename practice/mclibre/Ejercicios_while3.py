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

"""     Ejercicio 3: azar del 1 al 6 con 2 jugadores
activador = True
suma_jugador1 = 0
suma_jugador2 = 0
while activador:
    jugador1 = random.randint(1, 6)
    jugador2 = random.randint(1, 6)
    suma_jugador1 += jugador1
    suma_jugador2 += jugador2
    print("Jugador 1: ", jugador1, "\nJugador 2: ", jugador2)
    print("Suma jugador 1: ", suma_jugador1, "\nSuma jugador 2: ", suma_jugador2)
    keep = input("Si desea terminar el programa pulse intro...")
    if not keep:
        activador = False
"se puede simplificar la anidación de los 3 casos de la siguiente forma"
'print("Gana jugador 1" if jugador1 > jugador2 else "Gana jugador 2" if jugador2 > jugador1 else "Empate")'
if suma_jugador1 > suma_jugador2:
    print("Gana jugador 1")
elif suma_jugador2 > suma_jugador1:
    print("Gana jugador 2")
else:
    print("Empate")
"""

"""     Ejercicio 4: azar del 1 al 6 con 2 jugadores y eleccion de turno
activador = True
suma_jugador1 = 0
suma_jugador2 = 0
while activador:
    jugador1 = 0
    jugador2 = 0
    player1_turn = input("Turno jugador 1(intro para tirar dado): ")
    if not player1_turn:
        jugador1 = random.randint(1, 6)
        suma_jugador1 += jugador1
    player2_turn = input("Turno jugador 2(intro para tirar dado): ")
    if not player2_turn:
        jugador2 = random.randint(1, 6)
        suma_jugador2 += jugador2
    print("Jugador 1: ", jugador1, "\nJugador 2: ", jugador2)
    print("Suma jugador 1: ", suma_jugador1, "\nSuma jugador 2: ", suma_jugador2)
    keep_playing = input("Si desea terminar el programa pulse intro...")
    if not keep_playing:
        activador = False
"se puede simplificar la anidación de los 3 casos de la siguiente forma"
'print("Gana jugador 1" if jugador1 > jugador2 else "Gana jugador 2" if jugador2 > jugador1 else "Empate")'
if suma_jugador1 > suma_jugador2:
    print("Gana jugador 1")
elif suma_jugador2 > suma_jugador1:
    print("Gana jugador 2")
else:
    print("Empate")
"""

"""     Ejercicio 5: programa anterior con limite de 20pts
activador = True
suma_jugador1 = 0
suma_jugador2 = 0
while activador:
    jugador1 = 0
    jugador2 = 0
    player1_turn = input("Turno jugador 1(intro para tirar dado): ")
    if not player1_turn:
        jugador1 = random.randint(1, 6)
        suma_jugador1 += jugador1
    player2_turn = input("Turno jugador 2(intro para tirar dado): ")
    if not player2_turn:
        jugador2 = random.randint(1, 6)
        suma_jugador2 += jugador2
    print("Jugador 1: ", jugador1, "\nJugador 2: ", jugador2)
    print("Suma jugador 1: ", suma_jugador1, "\nSuma jugador 2: ", suma_jugador2)
    keep_playing = input("Si desea terminar el programa pulse intro...")
    if not keep_playing:
        activador = False
"se puede simplificar la anidación de los 3 casos de la siguiente forma"
'print("Gana jugador 1" if jugador1 > jugador2 else "Gana jugador 2" if jugador2 > jugador1 else "Empate")'
if suma_jugador1 > 20 and suma_jugador2 > 20:
    print("No hay ganadores, ambos excedieron 20pts...")
elif suma_jugador1 > suma_jugador2 or suma_jugador2 > 20:
    print("Gana jugador 1")
elif suma_jugador2 > suma_jugador1 or suma_jugador1 > 20:
    print("Gana jugador 2")
else:
    "unexpected case"
"""

"""     Ejercicio 6: tres numeros al azar del 1 al 6"""
activador = True
while activador:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    print("Numero 1: ", num1, "\nNumero 2: ", num2, "\nNumero 3: ", num3)
    keep_playing = input("Si desea terminar el programa pulse intro...")
    if not keep_playing:
        activador = False