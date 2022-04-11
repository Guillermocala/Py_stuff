class Clase:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def getData(self):
        return vars(self)

    def setData(self, nombre = None, apellido = None):
        if nombre is not None and apellido is not None:
            print("ingreso ambos argumentos")
        elif nombre is not None:
            print("ingreso nombre")
        elif apellido is not None:
            print("ingreso apellido")
        else:
            print("no ingreso nada")


obj = Clase("guillermo", "cala")
print(obj.getData())
obj.setData()