"""     Ejercicio 1: cuadrados
def cuadrados(numero):
    dic_res = {}
    for i in range(numero):
        dic_res[i] = i**2
    return dic_res

limite = int(input("Ingrese el limite: "))
diccionario = cuadrados(limite)
print(diccionario)
"""

"""     Ejercicio 2: ocurrencias cadena"""
def ocurrencias(cadena):
    dic_res = {}
    for item in cadena:
        dic_res[item] = cadena.count(item)
    return dic_res

cadena = input("Ingrese una cadena: ")
diccionario = ocurrencias(cadena)
print(diccionario)