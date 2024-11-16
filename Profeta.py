from Covenant import Covenant

class Profeta(Covenant):
    def __init__(self):
        Covenant.__init__(self)
        self.__mision = ""
        self.__nombre_profeta = ""

        #setters y getters

    def get_mision(self):
        return self.__mision

    def get_nombre_profeta(self):
        return self.__nombre_profeta


    def set_mision(self, mision):
        self.__mision = mision

    def set_nombre_profeta(self, nombre_profeta):
        self.__nombre_profeta = nombre_profeta

    # metodos de clase

    def mandar_mision(self):
        print("El dolor y la muerte son solo el preludio de la ascensión")

    def obtener_reliquia(self):
        print("Manto de los Forerunners obtenido")

