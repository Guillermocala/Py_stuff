def datos_all(item):
    item.show_data()
    
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def show_data(self):
        print(vars(self))

class Gato:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def show_data(self):
        print(vars(self))

class Leon:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def show_data(self):
        print(vars(self))

animales = [Perro("perrito", "labrador"), Gato("gatito", "albino"), Leon("leonsito", "selvatico")]
for item in animales:
    datos_all(item)