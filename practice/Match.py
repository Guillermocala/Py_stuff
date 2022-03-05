def saludo(nombre):
    match nombre: 
        case "guillermo":
            return "hola, guillermo"
        case "carlos":
            return "hola, carlos"
        case _:
            return ("No reconozco tu nombre. Hola, " + nombre)

def saludo2(nombre):
    match nombre: 
        case "Carlos" | "Juan" | "Gustavo":
            return ("Eres uno de mis amigos, hola " + nombre)
        case _:
            return ("No reconozco tu nombre. Hola, " + nombre)

def saludo3(nombre):
    match nombre: 
        case "Carlos" | "Juan" | "Gustavo" if "s" in nombre:
            return ("Eres uno de mis amigos, hola " + nombre + ". y tu nombre tiene una s")
        case _:
            return ("No reconozco tu nombre. Hola, " + nombre)


nombre = input("Ingresa tu nombre: ")
print(saludo3(nombre))