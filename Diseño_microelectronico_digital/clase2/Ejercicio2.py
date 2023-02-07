# Cree un programa que lea la longitud y el ancho del campo de un
# agricultor del usuario en pies. Mostrar el área del campo en acres.
# 43.560 pies cuadrados en un acre.

def main():
    print("\t\tArea de campo en acres(Unidad de ingreso Pies)")
    ancho = float(input("Ingrese el ancho: "))
    largo = float(input("Ingrese el largo: "))
    area_acres = (ancho / 43560) * (largo / 43560)
    print("El area en acres es: ", area_acres)

if __name__ == "__main__":
    main()