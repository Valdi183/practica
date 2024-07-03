from EstrellaDeLaMuerte import EstrellaDeLaMuerte

class NavePequeña(EstrellaDeLaMuerte):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.puntos_de_vida = 100

class NaveGrande(EstrellaDeLaMuerte):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.puntos_de_vida = 500