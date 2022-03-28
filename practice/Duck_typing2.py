def saludar(item):
    item.say_hi()
    
class Matematico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.caracteristica = 2
    
    def say_hi(self):
        print("Hola, mi nombre es {nombre} y {multiplo}x7 es: {resultado}".format(nombre = {self.nombre}, multiplo = {self.caracteristica} * 2, resultado = 3 * 7))

class Criptografo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.caracteristica = "mapas del tesoro"
    
    def say_hi(self):
        print("Hola, mi nombre es {nombre} y mi especialidad es: {especialidad}".format(nombre = self.nombre, especialidad = self.especialidad))

class Repartidor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tiempo_promedio = 30
    
    def say_hi(self):
        print("Hola, mi nombre es {nombre} y mi tiempo de entrega promedio es: {tiempo}".format(nombre = self.nombre, tiempo = self.tiempo_promedio))

profesionales = [Matematico("Francisco"), Criptografo("Albert"), Repartidor("Peter")]
for item in profesionales:
    saludar(item)