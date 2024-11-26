from Profeta import Profeta

class Sangheilli(Profeta):
    def __init__(self):
        Profeta.__init__(self)
        self.__numero_mandibulas = 0

    #getters y setters

    def set_numero_mandibulas(self, numero_mandibulas):
        self.__numero_mandibulas = numero_mandibulas

    def get_numero_mandibulas(self):
        return self.__numero_mandibulas

    #metodos de clase
    def chillido(self):
        print("wort wort wort")
    def escudo_energetico(self):
        print("energia proyectada de manera corporal")

