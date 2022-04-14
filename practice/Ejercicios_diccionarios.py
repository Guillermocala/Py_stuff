import os
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

"""     Ejercicio 2: ocurrencias cadena
def ocurrencias(cadena):
    dic_res = {}
    for item in cadena:
        dic_res[item] = cadena.count(item)
    return dic_res

cadena = input("Ingrese una cadena: ")
diccionario = ocurrencias(cadena)
print(diccionario)
"""

"""     Ejercicio 3: precios frutas
precio_frutas = {'Banano':1400, 'Manzana':3000, 'Fresa':2000, 'Kiwi':4000}
print("Tienda Frutas\n", precio_frutas)
fruta = input("Ingrese el nombre de la fruta: ")
cant_vendida = int(input("Ingrese la cantidad vendida: "))
if fruta in precio_frutas:
    precio_final = precio_frutas[fruta] * cant_vendida
    if cant_vendida > 1:
        print(f"{cant_vendida} {fruta}s tienen un total de: {precio_final}")
    else:
        print(f"{cant_vendida} {fruta} tiene un total de: {precio_final}")
else:
    print("Fruta no encontrada")
"""

"""     Ejercicio 4: notas alumnos
def ingresar_alumnos(cant_alumnos):
    dic_res = {}
    cont = 0
    while cont < cant_alumnos:
        notas = []
        nombre = input("Nombre alumno: ")
        if nombre not in dic_res:
            while True:
                nota = float(input("Ingrese nota: "))
                if nota >= 0:
                    notas.append(nota)
                else:
                    break
            dic_res[nombre] = notas
            cont += 1
        else:
            print("Alumno ya ingresado!")
    return dic_res

def diccionario_nota_media(diccionario):
    dic_res = {}
    for key, values in diccionario.items():
        cantidad = len(values)
        suma = 0
        for item in values:
            suma += item
        media = suma/cantidad
        dic_res[key] = media
    return dic_res

cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))
diccionario = ingresar_alumnos(cant_alumnos)
print("Diccionario notas\n", diccionario)
diccionario_media = diccionario_nota_media(diccionario)
print("Diccionario notas promedio\n", diccionario_media)
"""

"""     Ejercicio 5: agenda"""
def ingresar(diccionario):
    nombre = input("Ingrese el nombre: ")
    if nombre in diccionario:
        print(diccionario[nombre])
        modificar = input("Desea modificar el telefono? (S/N): ")
        if modificar in "Ss":
            nuevo_telefono = int(input("Ingrese el nuevo telefono: "))
            diccionario[nombre] = nuevo_telefono
    else:
        telefono = int(input("Ingrese el telefono: "))
        diccionario[nombre] = telefono

def buscar(diccionario, data):
    encontrado = False
    for key, value in diccionario.items():
        if key.removeprefix(data) != key:
            print(f"Nombre: {key} - telefono: {value}")
            encontrado = True
    if not encontrado:
        print("No encontrado")

def listar(diccionario):
    for key, value in diccionario.items():
        print(f"Nombre: {key} - telefono: {value}")

def menu(diccionario):
    activador = True
    while activador:
        os.system("cls")
        print("""
                MI AGENDA
            1-Añadir/modificar
            2-Buscar
            3-Borrar
            4-Listar
            0-Salir
        """)
        opcion = int(input("Ingrese la opción: "))
        match opcion:
            case 1:
                print("\tAñadir/modificar")
                ingresar(diccionario)
            case 2:
                print("\tBuscar")
                if diccionario:
                    cadena = input("Ingrese una cadena(nombre/prefijo): ")
                    buscar(diccionario, cadena)
                else:
                    print("Agenda vacía!")
                pass
            case 3:
                print("\tBorrar")
                if diccionario:
                    nombre = input("Ingrese el nombre: ")
                    if nombre in diccionario:
                        modificar = input("Desea borrar el contacto? (S/N): ")
                        if modificar in "Ss":
                            del diccionario[nombre]
                            print("Contacto borrado!")
                    else:
                        print("No encontrado")
                else:
                    print("Agenda vacía!")
            case 4:
                print("\tListar")
                if diccionario:
                    listar(diccionario)
                else:
                    print("Agenda vacía!")
            case 0:
                print("\tSalir")
                activador = False
            case _:
                print("excepcion match case -> menu")
        sleep = input("Presione una tecla para continuar")

agenda = {}
menu(agenda)