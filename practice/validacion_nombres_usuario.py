def validador(nombre):
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
elif validador(nombre) == True:
    print("El nombre del usuario debe ser alfanumerico(solo letras y numeros)")
else:
    print("Nombre de usuario valido!")