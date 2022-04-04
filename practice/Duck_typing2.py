def saludar(item):
    item.say_hi()
    
class Matematico:
    def __init__(self, nombre, num1, num2):
        self.nombre = nombre
        self.multiplo1 = num1
        self.multiplo2 = num2
    
    def say_hi(self):
        resultado = self.multiplo1 * self.multiplo2
        print(f"Hola, mi nombre es {self.nombre} y {self.multiplo1}x{self.multiplo2} es: {resultado}")

class Criptografo:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.caracteristica = especialidad
    
    def say_hi(self):
        print("Hola, mi nombre es {nombre} y mi especialidad es: {especialidad}".format(nombre = self.nombre, especialidad = self.caracteristica))

class Repartidor:
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo_promedio = float(tiempo)
    
    def say_hi(self):
        print("Hola, mi nombre es {nombre} y mi tiempo de entrega promedio es: {tiempo} minutos".format(nombre = self.nombre, tiempo = self.tiempo_promedio))

profesionales = [Matematico("Francisco", 4, 20), Criptografo("Albert", "mapas del tesoro"), Repartidor("Peter", 20)]
for item in profesionales:
    saludar(item)