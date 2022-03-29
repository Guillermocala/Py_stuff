def saludar(item):
    item.say_hi()
    
class Matematico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.multiplo1 = 2
        self.multiplo2 = 7
    
    def say_hi(self):
        resultado = 2 * 7
        print(f"Hola, mi nombre es {self.nombre} y {self.multiplo1}x{self.multiplo2} es: {resultado}")

class Criptografo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.caracteristica = "mapas del tesoro"
    
    def say_hi(self):
        print("Hola, mi nombre es {nombre} y mi especialidad es: {especialidad}".format(nombre = self.nombre, especialidad = self.caracteristica))

class Repartidor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tiempo_promedio = 30
    
    def say_hi(self):
        print("Hola, mi nombre es {nombre} y mi tiempo de entrega promedio es: {tiempo}".format(nombre = self.nombre, tiempo = self.tiempo_promedio))

profesionales = [Matematico("Francisco"), Criptografo("Albert"), Repartidor("Peter")]
for item in profesionales:
    saludar(item)