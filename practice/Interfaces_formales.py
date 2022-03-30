from abc import abstractmethod, ABCMeta

class Mando(metaclass=ABCMeta):
    @abstractmethod
    def siguiente_canal(self):
        pass

    @abstractmethod
    def canal_anterior(self):
        pass

    @abstractmethod
    def subir_volumen(self):
        pass

    @abstractmethod
    def bajar_volumen(self):
        pass

class MandoSamsung(Mando):
    def siguiente_canal(self):
        print("Samsung->Siguiente")
    def canal_anterior(self):
        print("Samsung->Anterior")
    def subir_volumen(self):
        print("Samsung->Subir")
    def bajar_volumen(self):
        print("Samsung->Bajar")

class MandoLG(Mando):
    def siguiente_canal(self):
        print("LG->Siguiente")
    def canal_anterior(self):
        print("LG->Anterior")
    def subir_volumen(self):
        print("LG->Subir")
    def bajar_volumen(self):
        print("LG->Bajar")

mando_samsung = MandoSamsung()
mando_samsung.siguiente_canal()
mando_samsung.canal_anterior()
mando_samsung.subir_volumen()
mando_samsung.bajar_volumen()
mando_lg = MandoLG()
mando_lg.siguiente_canal()
mando_lg.canal_anterior()
mando_lg.subir_volumen()
mando_lg.bajar_volumen()