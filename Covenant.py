class Covenant:
    def __init__(self):
        self.__reliquias = ""
        self.__nivel_autoridad = 0
        self.__tiempo_estimado = 0
        self.__rango = 0

       # setters y getters

    def get_reliquias(self):
        return self.__reliquias
    def get_nivel_autoridad(self):
        return self.__nivel_autoridad
    def get_tiempo_estimado(self):
        return self.__tiempo_estimado
    def get_rango(self):
        return self.__rango

    def set_reliquias(self, reliquias):
        self.__reliquias = reliquias
    def set_nivel_autoridad(self, nivel_autoridad):
        self.__nivel_autoridad = nivel_autoridad
    def set_tiempo_estimado(self, tiempo_estimado):
        self.__tiempo_estimado = tiempo_estimado
    def set_rango(self, rango):
        self.__rango = rango

        #metodos de clase

    def activar_anillo(self):
        print("se activo un anillo")

    def crear_naves(self):
        print("se mandan tropas a un planeta")

    def evangelizar_especies(self):
        print("haciendo un trato con esta especie pacifica")