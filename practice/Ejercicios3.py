"""     Ejercicio 1: reino del dragon"""
import random, time

def introduccion():
    print("""       REINO DEL DRAGON
    Estamos en una tierra llena de dragones. Delante nuestro,
    se ven dos cuevas. En una cueva, el dragon es amigable
    y compartira el tesoro contigo. El otro dragon
    es codicioso y hambriento, y te va a comer ni bien te vea.
    """)

def cambiar_cueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        cueva = input("A que cueva quieres entrar? 1 o 2?: ")
    return cueva

def chequea_cueva(cueva):
    print("Te acercas a la cueva...")
    time.sleep(2)
    print("Esta oscuro y tenebroso...")
    time.sleep(2)
    print("Un gran dragon salta delante tuyo, abre su boca y...")
    time.sleep(2)
    suerte = random.randint(1, 2)
    if cueva == 1:
        print("Te engrega el tesoro...")
        return 100
    else:
        print("El dragon te come de un bocado...")
        return 0

def verificador(puntos):
    print(f"GAME OVER.... obtuviste: {puntos} puntos")
    while True:
        opcion = input("Quieres jugar de nuevo?(si/no): ")
        match opcion:
            case "si":
                return True
            case "no":
                return False
            case _: 
                print("Opcion invalida")

activador = "si"
while activador == "si":
    puntos = 0
    introduccion()
    num_caverna = (cambiar_cueva())
    puntos_obtenidos = (chequea_cueva(num_caverna))
    while  puntos_obtenidos == 100:
        puntos += puntos_obtenidos
        num_caverna = (cambiar_cueva())
        puntos_obtenidos = (chequea_cueva(num_caverna))

    if not(verificador(puntos)):
        break