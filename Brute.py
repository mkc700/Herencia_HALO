from Profeta import Profeta
from Desterrado import Desterrado

class Brute(Profeta,Desterrado):
    def __init__(self):
        Profeta.__init__(self)
        Desterrado.__init__(self)
        self.__nivel_ira = 0
        self.__grosor_piel = 0

    #setters y getters

    def set_nivel_ira(self, nivel_ira):
        self.__nivel_ira = nivel_ira
    def set_grosor_piel(self, grosor_piel):
        self.__grosor_piel = grosor_piel

    def get_nivel_ira(self):
        return self.__nivel_ira
    def get_grosor_piel(self):
        return self.__grosor_piel

    #metodos

    def ataque_brutal(self):
        print("ataque envolvedor que noquea al contrincate")
    def entrar_en_furia(self):
        print("se enciende una llama dentro de la mente del brute, una furia sin igual")

        