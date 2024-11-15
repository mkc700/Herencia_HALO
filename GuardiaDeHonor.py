from Brute import Brute

class GuardiaDeHonor(Brute):
    def __init__(self):
        Brute.__init__(self)
        self.__medallas = 0
        self.__armadura_especial = ""

    #getters y setters

    def get_medallas(self):
        return self.__medallas
    def get_armadura_especial(self):
        return self.__armadura_especial

    def set_medallas(self, medallas):
        self.__medallas = medallas
    def set_armadura_especial(self, armadura_especial):
        self.__armadura_especial = armadura_especial

    #metodos de clase

    def defensa_feroz(self):
        print("el guardia arriesgara su vida con tal la de preservar la del profeta")
    def cerrar_cobertura(self):
        print("resguardara la vision del profeta para que pueda salir sin afectaciones")