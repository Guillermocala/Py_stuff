def saludo(name):
    return ("Hola, " + name)

def saludo2(name = 'guillermo'):
    return("Saludo predeterminado. Hola, " + name)

def confirmacion(texto):
    if texto in ("y", "ye", "yes"):
        return("Ok, positivo")
    elif texto in ("n", "no", "nop"):
        return("Ok, negativo")
    else:
        return("Ok, no definido")
def listaNombres(nombre, lista = []):
    lista.append(nombre)
    return lista

def listaNombresNoCompartida(nombre, lista = None):
    "esto es lo mismo que la anterior pero sin guardar los datos anteriores"
    if lista == none:
        lista = []
    lista.append(nombre)
    return lista

print(saludo("Andrea"))
referencia = saludo
print(referencia("Guillermo"))
print(saludo2())
print(saludo2("Javier"))
print(listaNombres("guillermo"))
print(listaNombres("andrea"))
print(listaNombres("gustavo"))
