"""     Ejercicio 1: max_in_list()
def max_in_list(lista):
    acumulador = 0
    for item in lista:
        if item > acumulador:
            acumulador = item
    return acumulador

lista = [23, 1, 12, 8, 19]
print("El mayor de la lista es: ", max_in_list(lista))
"""

"""     Ejercicio 2: mas_larga()
def mas_larga(lista):
    acumulador = 0
    palabra_ganadora = ""
    for item in lista:
        if len(item) > acumulador:
            acumulador = len(item)
            palabra_ganadora = item
    return palabra_ganadora

lista = ["Juan", "Hernesto", "Perensejo", "Guillermo"]
print("La palabra mas larga es: ", mas_larga(lista))
"""

"""     Ejercicio 3: filtrar_palabras()
def filtrar_palabras(lista, cantidad):
    resultado = []
    for item in lista:
        if len(item) == cantidad:
            resultado.append(item)
    return resultado

lista = ["Juan", "Hernesto", "Jose", "Toti", "Perensejo", "Guillermo"]
cantidad = int(input("Ingrese el numero de caracteres: "))
print("Las palabras filtradas son: ", filtrar_palabras(lista, cantidad))
"""

"""     Ejercicio 4: letras_mayusculas()
def cantidad_mayusculas(cadena):
    cantidad = 0
    for item in cadena:
        if item.isupper():
            cantidad += 1
    return cantidad

cadena = input("Ingrese una cadena de caracteres que contenga mayusculas: ")
print("La cantidad de mayus es: ", cantidad_mayusculas(cadena))
"""

"""     Ejercicio 5: binario_a_entero()
def binario_a_entero(numero):
    lista = [int(x) for x in str(numero)]
    lista.reverse()
    acumulador = 0
    for item in range(len(lista)):
        if lista[item] == 1:
            acumulador += 2 ** item
    return acumulador

numero_binario = input("Ingrese un numero binario: ")
print("El numero entero es: ", binario_a_entero(numero_binario))
"""

"""     Ejercicio 6: calcula_edad()
def ingresa_datos(cantidad):
    datos = {}
    for item in range(cantidad):
        nombre = input("Ingrese el nombre: ")
        anio = int(input("Ingrese el anio de nacimiento: "))
        datos[nombre] = anio
    return datos

def calcula_edad(lista, anio_actual):
    for x, y in lista.items():
        edad = anio_actual - y
        print("La edad de ", x, " es ", edad)

anio_actual = int(input("Ingrese el anio actual: "))
nombres = ingresa_datos(3)
calcula_edad(nombres, anio_actual)
"""

"""     Ejercicio 7: edades_superiores_20()
def edades_superiores_20(lista):
    cantidad = 0
    for item in lista:
        if 2022 - item > 20:
            cantidad += 1
    return cantidad

def ingresa_datos(cantidad):
    tupla_anios = ()
    for item in range(cantidad):
        anio = int(input(f"{item}- Ingrese el anio de nacimiento: "))
        tupla_anios = tupla_anios + (anio, )
    return tupla_anios

tupla = ingresa_datos(10)
print("La cantidad de mayores que 20 es: ", edades_superiores_20(tupla))
"""

"""     Ejercicio 8: filtro_nombres()
def filtro_nombres(lista, caracter):
    cantidad = 0
    for item in lista:
        if caracter in item:
            cantidad += 1
    return cantidad

lista = ["jose", "juan", "perensejo", "adriana", "gustavo"]
caracter = input("Ingrese el caracter para filtrar: ")
print("Hay ", filtro_nombres(lista, caracter), " nombres con dicho caracter")
"""

"""     Ejercicio 9: contar_vocales()
def contar_vocales(palabra):
    "lista = [a, e, i, o, u]"
    dic_contadores = {"a":0, "e":0, "i":0, "o":0, "u":0}
    for item in palabra:
        match item.lower():
            case 'a':
                dic_contadores["a"] = dic_contadores["a"] + 1
            case 'e':
                dic_contadores["e"] = dic_contadores["e"] + 1
            case 'i':
                dic_contadores["i"] = dic_contadores["i"] + 1
            case 'o':
                dic_contadores["o"] = dic_contadores["o"] + 1
            case 'u':
                dic_contadores["u"] = dic_contadores["u"] + 1
            case _:
                pass
    return dic_contadores

palabra = input("Ingrese una palabra: ")
dic_resultados = contar_vocales(palabra)
for x, y in dic_resultados.items():
    print("vocal: ", x, " cantidad: ", y)
"""

"""     Ejercicio 10: es_bisiesto()
def es_bisiesto(anio):
    resultado = None
    if anio % 4 == 0 and (not (anio % 100 == 0)):
        resultado = True
    elif anio % 400 == 0:
        resultado = True
    else:
        resultado = False
    return resultado

dato = int(input("Ingrese el anio: "))
if es_bisiesto(dato):
    print("anio bisiesto")
else:
    print("anio no bisiesto")
"""