class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo

    @mi_atributo.setter
    def mi_atributo(self, valor):
        if valor != "":
            print("Modificando el valor")
            self.__mi_atributo = valor
        else:
            print("Error está vacío")

obj = Clase("Guillermo")
print(obj.mi_atributo)
obj.mi_atributo = "No soy guillermo"
print(obj.mi_atributo)