print("It's a prime number?")
num = int(input("Input the number: "))
cont = 0
#el rango funciona en base a (rango inicial, rango final, valor de incremento/decremento)
#para que tome el ultimo valor debo sumarle 1
for i in range(1, num + 1):
    if num % i == 0:
        cont = cont + 1
if cont == 2:
    print("It's a prime number!")
else:
    print("It's not a prime number!")
