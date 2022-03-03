def alfanumerico(nombre):
	numeros = "1234567890"
	for caracter in nombre:
		if caracter in numeros:
			return True
	return False
def caracteresIncorrectos(nombre):
    caracteresDisponibles = "1234567890abcdefghijklmnopqrstuvwxyz"
    for caracter in nombre:
        if not caracter in caracteresDisponibles:
            return True
    return False
        
nombre = input("Ingrese el nombre del usuario: ")
if len(nombre) < 6:
		print("El nombre del usuario debe contener al menos 6 caracteres")
elif len(nombre) > 12:
		print("El nombre del usuario no puede contener mas de 12 caracteres")
elif alfanumerico(nombre) == False:
    print("El nombre del usuario debe ser alfanumerico")
elif caracteresIncorrectos(nombre) == True:
    print("El nombre del usuario solo debe contener letras y numeros")
else:
    print("Nombre de usuario valido!")