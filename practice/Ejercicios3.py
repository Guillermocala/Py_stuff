'''     Ejercicio 1: reino del dragon
import random, time

def introduccion():
    print("""               REINO DEL DRAGON
    Estamos en una tierra llena de dragones. Delante nuestro,
    se ven dos cuevas. En una cueva, el dragon es amigable
    y compartira el tesoro contigo. El otro dragon
    es codicioso y hambriento, y te va a comer ni bien te vea.
    """)

def cambiar_cueva():
    cueva = 0
    while cueva != 1 and cueva != 2:
        cueva = int(input("A que cueva quieres entrar? 1 o 2?: "))
    return cueva

def chequea_cueva(cueva):
    print("Te acercas a la cueva...")
    time.sleep(2)
    print("Esta oscuro y tenebroso...")
    time.sleep(2)
    print("Un gran dragon salta delante tuyo, abre su boca y...")
    time.sleep(2)
    suerte = random.randint(1, 2)
    if cueva == suerte:
        print("Te engrega el tesoro...(+100pts)")
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

'''

"""     Ejercicio 2: MASTER MIND
import random
def ingresa_numero():
    len_cadena = 0
    while not(len_cadena in range(2, 9)):
        len_cadena = int(input("Ingrese la longitud del numero(2 a 9): "))
    
    num_random = str(random.randint(0, 999999999))
    resultado = int(num_random[:len_cadena])
    return resultado

def verificador(num_pendiente):
    num_ingresado = int(input("Intenta adivinar el numero: "))    
    while len(str(num_ingresado)) != len(str(num_pendiente)):
        print("Ha ingresado un numero de diferente tamanio")
        num_ingresado = int(input("Intenta adivinar el numero: "))
    return num_ingresado

def master_mind(num_ingresado, num_pendiente):
    lista_num_ingr = [int(x) for x in str(num_ingresado)]
    lista_num_pend = [int(x) for x in str(num_pendiente)]
    cantidad = 0
    for x in range(len(lista_num_ingr)):
        if lista_num_ingr[x] == lista_num_pend[x]:
            cantidad += 1
    return cantidad

num_generado = ingresa_numero()
activador = True
num_ingresado = verificador(num_generado)
cantidad = master_mind(num_ingresado, num_generado)
while activador:
    if len(str(num_ingresado)) != cantidad:
        print("Con", num_ingresado, " has adivinado: ", cantidad)
        num_ingresado = verificador(num_generado)
        cantidad = master_mind(num_ingresado, num_generado)
    else:
        print("Con", num_ingresado, " has adivinado: ", cantidad)
        print("Felicidades, has ganado!")
        activador = False
"""

"""     Ejercicio 3: Palabras que riman
def palabras_riman(palabra1, palabra2):
    if palabra1[len(palabra1) - 3:] == palabra2[len(palabra2) - 3:]:
        print("Las palabras riman")
    elif palabra1[len(palabra1) - 2:] == palabra2[len(palabra2) - 2:]:
        print("Las palabras riman un poco")
    else:
        print("Las palabras no riman")

palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")
palabras_riman(palabra1, palabra2)
"""

"""     Ejercicio 4: convertidor"""