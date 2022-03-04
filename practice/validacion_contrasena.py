def validador(contrasena):
    numeros = "1234567890"
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    tieneMinusculas = False
    tieneMayusculas = False
    caracterEspecial = False
    tieneNumeros = False
    for caracter in contrasena:
        if caracter in numeros:
            tieneNumeros = True
        elif caracter in alfabeto:
            tieneMinusculas = True
        elif caracter in alfabeto.upper():
            tieneMayusculas = True
        else:
            caracterEspecial = True
    if (tieneMayusculas and tieneMinusculas and tieneNumeros and caracterEspecial):
        return True
    else:
        return False
        
def espacios(contrasena):
    whiteSpace = " "
    if whiteSpace in contrasena:
        return True
    else:
        return False

password = input("Ingrese la contrasena: ")
if len(password) < 8:
	print("La contrasena debe tener al menos 8 caracteres")
elif espacios(password) == True:
    print("La contrasena no puede tener espacios en blanco")    
elif validador(password) == False:
    print("La contrasena debe tener minusculas, mayusculas, numeros y al menos 1 caracter especial")
else:
    print("Contrasena valida!")