import random
print("\tADIVINA EL NUMERO...")
limite = int(input("Ingrese el limite(mayor a 1): "))
while limite <= 1:
    print("Dato incorrecto!")
    limite = int(input("Ingrese el limite(mayor a 1): "))
num = int(random.randint(1, limite))
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
input("Pulsa enter para continuar")
