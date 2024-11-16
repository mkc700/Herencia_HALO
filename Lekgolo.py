from Profeta import Profeta

class Lekgolo(Profeta):
    def __init__(self):
        Profeta.__init__(self)
        self.__no_larvas = 0


    #getters y setters

    def get_no_larvas(self):
        return self.__no_larvas

    def set_no_larvas(self, value):
        self.__no_larvas = value

    #metodos de clases

    def activa_formacion_defensiva(self):
        print("* se inclina ligeramente para proteger sus organos vitales")

    def ataque_de_combustible(self):
        print("ataque de energia de combustible neon")


