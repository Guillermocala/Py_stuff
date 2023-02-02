# Escriba un programa que solicite una letra del alfabeto e indique sí es
# una vocal o una consonante, si no es ninguna de las dos, entonces
# debe indicar que ese carácter no es válido.

def main():
    print("\t\tConsonante o vocal")
    letra = input("Ingrese una letra del alfabeto: ")
    # con la funcion lower nos aseguramos de verificar correctamente
    # para no añadir las mismas letras en mayusculas, una validacion
    # basica
    if letra.lower() in ["a", "e", "i", "o", "u"]:
        print("Es vocal")
    elif letra.lower() in ["b", "c", "d", "f", "g", "h", "j", "k",
                            "l", "m", "n", "p", "q", "r", "s", "t",
                            "v", "x", "y", "z"]:
        print("Es consonante")
    else:
        print("Caracter no valido!")

if __name__ == "__main__":
    main()