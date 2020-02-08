import random
num = int(random.randint(0,10))
print("\tADIVINA EL NUMERO...")
while True:
    x = int(input("Ingresa un numero: "))
    if x == num:
        print("Adivinaste!")
        break
    elif x < num:
        print("es menor")
    else:
        print("es mayor")
print("Juego terminado!")
