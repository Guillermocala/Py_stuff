# Escriba un programa que le pida al usuario que ingrese el ancho y el
# largo de una habitación. Una vez leídos los valores, su programa
# debería calcular y mostrar el área de la habitación. La longitud y el
# ancho se ingresarán como números de punto flotante. Incluya
# unidades en su mensaje de solicitud y salida; pies o metros.

def main():
    print("\t\tCalculo de area en metros")
    ancho = float(input("Ingrese el ancho: "))
    largo = float(input("Ingrese el largo: "))
    area = ancho * largo
    print("El area es: ", area)

if __name__ == "__main__":
    main()