import os
import re
def menu():
    os.system("cls")
    print(
        """
        1-crear producto
        2-modificar producto
        3-buscar producto
        4-mostrar lista productos
        5-agregar cantidad inventario
        6-sacar cantidad inventario
        7-salir
    """)
    opcion = input("ingrese la opción: ")
    return opcion

def crear(lista):
    temp = True
    while temp:
        codigo = input("ingrese el codigo: ")
        for producto in lista:
            if producto[0] == codigo:
                print("el codigo ya existe")
                temp = True
                break
        else:
            temp = False
        if re.search('[a-z]', codigo.lower()) == None:
            print("código inválido, debe tener al menos una letra")
            temp = True
    nombre = input("ingrese el nombre: ")
    cantidad = 0
    costoUnitario = int(input("ingrese el costo unitario: "))
    lista.append([codigo, nombre, cantidad, costoUnitario])

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
        
def operaciones(lista, operacion):
    codigo = input("ingrese el codigo: ")
    for producto in lista:
        if producto[0] == codigo:
            if operacion == 1:
                #modificar
                producto[1] = input("ingrese el nuevo nombre: ")
                producto[3] = int(input("ingrese el nuevo costo unitario: "))
                break
            elif operacion == 2:
                #buscar
                costoTotal = producto[2] * producto[3]
                print(f"""
                    codigo: {producto[0]}
                    nombre: {producto[1]}
                    cantidad: {producto[2]}
                    costo unitario: {producto[3]}
                    costo total: {costoTotal}""")
                break
            elif operacion == 3:
                #agregarCantidad
                cantidad = int(input("ingrese la cantidad: "))
                producto[2] += cantidad
                break
            elif operacion == 4:
                #sacarCantidad
                cantidad = int(input("ingrese la cantidad: "))
                resta = producto[2] - cantidad
                if resta < 0:
                    producto[2] = 0
                else:
                    producto[2] = resta
                break
            else:
                print("error en la funcion operaciones")
                break
    else:
        print("no encontrado")

productos = [["A12", "platano", 0, 2000], ["A23", "amarillo", 2, 2000], ["A52", "salsa", 6, 2000]]
activador = True
while(activador):
    temp = menu()
    if temp == '1':
        print("     crear producto")
        crear(productos)
    elif temp == '2':
        print("     modificar producto")
        operaciones(productos, 1)
    elif temp == '3':
        print("     mostrar producto")
        operaciones(productos, 2)
    elif temp == '4':
        print("     mostrar lista productos ")
        mostrar(productos)
    elif temp == '5':
        print("     agregar cantidad inventario")
        operaciones(productos, 3)
    elif temp == '6':
        print("     sacar cantidad inventario")
        operaciones(productos, 4)
    elif temp == '7':
        print("     el programa se cerrara")
        break
    else:
        print("opcion erronea")
    pausa = input("presione una tecla para continuar...")