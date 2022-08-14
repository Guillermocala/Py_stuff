import random
import time
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

"""     Ejercicio 6: tres numeros al azar del 1 al 6
activador = True
while activador:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    print("Numero 1: ", num1, "\nNumero 2: ", num2, "\nNumero 3: ", num3)
    keep_playing = input("Si desea terminar el programa pulse intro...")
    if not keep_playing:
        activador = False
"""

"""     Ejercicio 7: anterior. Extra con 2 o 3 nums iguales
activador = True
while activador:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    print("Numero 1: ", num1, "\nNumero 2: ", num2, "\nNumero 3: ", num3)
    if num1 == num2 and num1 == num3:
        print("tres numeros iguales")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("dos numeros iguales")
    keep_playing = input("Si desea terminar el programa pulse intro...")
    if not keep_playing:
        activador = False
"""

"""     Ejercicio 8: maquina tragaperras v1
print("\t\tMAQUINA TRAGAPERRAS V1")
coins = 1
activador = True
while activador:
    coins -= 1
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    print("Numero 1: ", num1, "\nNumero 2: ", num2, "\nNumero 3: ", num3)
    if num1 == num2 and num1 == num3:
        coins += 5
        print("tres numeros iguales, usted gana 5 monedas.")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        coins += 2
        print("dos numeros iguales, usted gana 2 monedas.")
    print("Usted tiene: ", coins , " monedas.")
    keep_playing = input("Si desea salir del juego pulse intro...")
    if not keep_playing:
        activador = False
"""

"""     Ejercicio 9: maquina tragaperras v2(final)
print("\t\tMAQUINA TRAGAPERRAS V2")
coins = int(input("Ingrese la cantidad de monedas: "))
while coins < 1:
    print("No puede jugar con menos de 1 moneda!")
    coins = int(input("Ingrese la cantidad de monedas: "))
activador = True
while activador:
    coins -= 1
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    print("Numero 1: ", num1, "\nNumero 2: ", num2, "\nNumero 3: ", num3)
    if num1 == num2 and num1 == num3:
        coins += 5
        print("tres numeros iguales, usted gana 5 monedas.")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        coins += 2
        print("dos numeros iguales, usted gana 2 monedas.")
    print("Usted tiene: ", coins , " monedas.")
    if coins == 0:
        break
    else:
        keep_playing = input("Si desea salir del juego pulse intro...")
        if not keep_playing:
            activador = False
print("\tGAME OVER\nUsted termino con " ,coins, " monedas.")
"""

"""     Ejercicio 10: juego de sumas
print("\t\tJUEGO DE SUMAS V1\nDebe adiviar 5 sumas para ganar...")
intentos = 0
aciertos = 0
while aciertos < 5:
    intentos += 1
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    suma = num1 + num2
    print("intento ", intentos, "\n", num1, " + ", num2)
    respuesta = int(input("respuesta: "))
    if respuesta == suma:
        aciertos += 1
        print("Correcto!")
    else:
        print("Incorrecto!")
print("\tGAME OVER... te ha llevado ", intentos, " intentos!")
"""

"""     Ejercicio 11: juego de sumas con limite definido por usuario y cantidad de intentos
print("\t\tJUEGO DE SUMAS V2")
limite = int(input("Ingrese la cantidad de sumas objetivo: "))
while limite < 1:
    print("No puede jugar con menos de 1 pregunta!")
    limite = int(input("Ingrese la cantidad de sumas objetivo: "))
intentos = 0
aciertos = 0
while aciertos < limite:
    intentos += 1
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    suma = num1 + num2
    print("intento ", intentos, "\n", num1, " + ", num2)
    respuesta = int(input("respuesta: "))
    if respuesta == suma:
        aciertos += 1
        print("Correcto!")
    else:
        print("Incorrecto!")
print("\tGAME OVER... te ha llevado ", intentos, " intentos!")
"""

"""     Ejercicio 12: anterior añadiendo tiempo de juego
print("\t\tJUEGO DE SUMAS V3")
limite = int(input("Ingrese la cantidad de sumas objetivo: "))
while limite < 1:
    print("No puede jugar con menos de 1 pregunta!")
    limite = int(input("Ingrese la cantidad de sumas objetivo: "))
intentos = 0
aciertos = 0
inicio_juego = time.time()
while aciertos < limite:
    intentos += 1
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    suma = num1 + num2
    print("intento ", intentos, "\n", num1, " + ", num2)
    respuesta = int(input("respuesta: "))
    if respuesta == suma:
        aciertos += 1
        print("Correcto!")
    else:
        print("Incorrecto!")
fin_juego = time.time()
tiempo_juego = int(fin_juego - inicio_juego)
print("\tGAME OVER... te ha llevado ", intentos, " intentos en ", tiempo_juego, " segundos!")
"""

"""     Ejercicio 13: anterior con repeticion de operaciones
print("\t\tJUEGO DE SUMAS V4")
limite = int(input("Ingrese la cantidad de sumas objetivo: "))
while limite < 1:
    print("No puede jugar con menos de 1 pregunta!")
    limite = int(input("Ingrese la cantidad de sumas objetivo: "))
intentos = 0
aciertos = 0
inicio_juego = time.time()
respuesta_rapida = 99999
while aciertos < limite:
    activador2 = True
    genera_nueva_suma = False
    intentos += 1
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    suma = num1 + num2
    print("intento ", intentos, "\n", num1, " + ", num2)
    tiempo_inicial_respuesta = time.time()
    respuesta = int(input("respuesta: "))
    while activador2:
        if respuesta == suma:
            tiempo_final_respuesta = time.time()
            print("Correcto!")
            aciertos += 1
            activador2 = False
        else:
            keep_playing = input("Incorrecto! presione intro si desea intentar de nuevo: ")
            if not keep_playing:
                intentos += 1
                print("intento ", intentos, "\n", num1, " + ", num2)
                tiempo_inicial_respuesta = time.time()
                respuesta = int(input("respuesta: "))
            else:
                activador2 = False
                genera_nueva_suma = True
    if not genera_nueva_suma:
        tiempo_respuesta = int(tiempo_final_respuesta - tiempo_inicial_respuesta)
        if tiempo_respuesta < respuesta_rapida:
            respuesta_rapida = tiempo_respuesta
fin_juego = time.time()
tiempo_juego = int(fin_juego - inicio_juego)
print("\tGAME OVER... te ha llevado ", intentos, " intentos en ", tiempo_juego, " segundos!")
print("La respuesta mas rapida fue en: ", respuesta_rapida, " segundos!")
"""

"""     Ejercicio 14: adivina el numero
print("\tADIVINA EL NUMERO V1")
print("Debera ingresar los valores entre los cuales adivinara el usuario...")
valor_inicial = int(input("Ingresa el valor inicial: "))
valor_final = int(input("Ingresa el valor final: "))
pendiente_adivinar = random.randint(valor_inicial, valor_final)
acierto = False
while not acierto:
    respuesta = int(input("Respuesta: "))
    if respuesta == pendiente_adivinar:
        acierto = True
        print("Has adivinado!")
    elif respuesta < pendiente_adivinar:
        print("Tu respuesta es muy pequeña...")
    elif respuesta > pendiente_adivinar:
        print("Tu respuesta es muy grande...")
    else:
        "unexpected case"
"""

"""     Ejercicio 15: adivina el numero v2"""
print("\tADIVINA EL NUMERO V2")
print("Debera ingresar los valores entre los cuales adivinara la computadora...")
valor_inicial = int(input("Ingresa el valor inicial: "))
valor_final = int(input("Ingresa el valor final: "))
while valor_final <= valor_inicial:
    print("El valor final no puede ser menor o igual al valor incial!")
    valor_final = int(input("Ingresa el valor final: "))
acierto = False
print("Piensa un numero entre ", valor_inicial, " y ", valor_final, " a ver si lo adivino.")
while not acierto:
    intento_adivinar = random.randint(valor_inicial, valor_final)
    respuesta = input(f"¿Es {intento_adivinar} ?: ")
    if respuesta.lower() == "igual":
        acierto = True
        print("Game over!")
    elif respuesta.lower() == "menor":
        valor_final = intento_adivinar - 1
    elif respuesta.lower() == "mayor":
        valor_inicial = intento_adivinar + 1
    else:
        "unexpected case"
