class Desterrado:
    def __init__(self):
        self.__cacique = ""
        self.__tecnologia = ""

    #getters y setters

    def get_cacique(self):
        return self.__cacique
    def get_tecnologia(self):
        return self.__tecnologia

    def set_cacique(self, cacique):
        self.__cacique = cacique
    def set_tecnologia(self, tecnologia):
        self.__tecnologia = tecnologia

    #metodos de clase

    def robar_territorio(self):
        print("se ha robado una cantidad x de territorios")

    def obtener_informacion_covenant(self):
        print("se han develado informacion importante para derrocar a uno de los profetas")
