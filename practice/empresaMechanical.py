import os
def menu():
    #para limpiar consola y quede ordenado
    os.system("cls")
    print(
        """
        1-crear producto
        2-modificar producto
        3-mostrar producto
        4-mostrar lista productos
        5-agregar cantidad inventario
        6-sacar cantidad inventario
        7-salir
    """)
    opcion = input("ingrese la opción: ")
    return opcion

def crear(lista):
    codigo = input("ingrese el codigo: ")
    nombre = input("ingrese el nombre: ")
    cantidad = 0
    costoUnitario = int(input("ingrese el costo unitario: "))
    #va a quedar como una lista(productos) que contiene items(producto)
    #y estos tienen codigo, nombre, etc. Es decir, una lista de listas
    lista.append([codigo, nombre, cantidad, costoUnitario])

def modificar(lista):
    codigo = input("ingrese el codigo: ")
    for producto in lista:
        if producto[0] == codigo:
            """estos prints de antes y despues es solo para tener
                mas control, se pueden borrar"""
            print(f"antes: {producto}")
            producto[1] = input("ingrese el nuevo nombre: ")
            producto[3] = int(input("ingrese el nuevo costo unitario: "))
            print(f"después: {producto}")
            break
    else:
        print("no encontrado")

def buscar(lista):
    codigo = input("ingrese el codigo: ")
    for producto in lista:
        if producto[0] == codigo:
            costoTotal = producto[2] * producto[3]
            print(f"""
                codigo: {producto[0]}
                nombre: {producto[1]}
                cantidad: {producto[2]}
                costo unitario: {producto[3]}
                costo total: {costoTotal}""")
            break
    else:
        print("no encontrado")
    
def mostrar(lista):
    for producto in lista:
        costoTotal = producto[2] * producto[3]
        print(f"""
            codigo: {producto[0]}
            nombre: {producto[1]}
            cantidad: {producto[2]}
            costo unitario: {producto[3]}
            costo total: {costoTotal}""")
        print("")

def agregarCantidad(lista):
    codigo = input("ingrese el codigo: ")
    for producto in lista:
        if producto[0] == codigo:
            print(f"antes: {producto}")
            cantidad = int(input("ingrese la cantidad: "))
            producto[2] += cantidad
            print(f"después: {producto}")
            break
    else:
        print("no encontrado")

def sacarCantidad(lista):
    codigo = input("ingrese el codigo: ")
    for producto in lista:
        if producto[0] == codigo:
            print(f"antes: {producto}")
            cantidad = int(input("ingrese la cantidad: "))
            """en caso de que ingrese una cantidad mayor a la que hay
                en el inventario ponemos 0, luego que se añadan las
                verificaciones se corrige para que no acepte un numero
                mayor a la cantidad que hay en el inventario"""
            resta = producto[2] - cantidad
            if resta < 0:
                producto[2] = 0
            else:
                producto[2] = resta
            print(f"después: {producto}")
            break
    else:
        print("no encontrado")

#aca le meto algunos valores x para ahorrar tiempo en la prueba del algoritmo
productos = [["12", "platano", 0, 2000], ["23", "amarillo", 2, 2000], ["52", "salsa", 6, 2000]]
activador = True
while(activador):
    temp = menu()
    if temp == '1':
        print("     crear producto")
        crear(productos)
    elif temp == '2':
        print("     modificar producto")
        modificar(productos)
    elif temp == '3':
        print("     mostrar producto")
        buscar(productos)
    elif temp == '4':
        print("     mostrar lista productos ")
        mostrar(productos)
    elif temp == '5':
        print("     agregar cantidad inventario")
        agregarCantidad(productos)
    elif temp == '6':
        print("     sacar cantidad inventario")
        sacarCantidad(productos)
    elif temp == '7':
        print("     el programa se cerrara")
        break
    else:
        print("opcion erronea")
    #no se hace nada con pausa, es solo una variable para frenar
    pausa = input("presione una tecla para continuar...")