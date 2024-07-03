from Planetas import PlanetaConcordia, PlanetaIlum, PlanetaKamino

class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_de_vida = 1000

    def destruir_planeta(self, planeta):
        if planeta.clasificacion <= self.puntos_de_vida:
            self.puntos_de_vida -= planeta.clasificacion
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}. Puntos de vida restantes: {self.puntos_de_vida}")
        else:
            print(f"La Estrella de la Muerte no puede destruir el planeta {planeta.nombre}. Puntos de vida insuficientes.")

if __name__ == "__main__":
    estrella_de_la_muerte = EstrellaDeLaMuerte()
    
    concordia = PlanetaConcordia()
    ilum = PlanetaIlum()
    kamino = PlanetaKamino()
    
    estrella_de_la_muerte.destruir_planeta(concordia)
    estrella_de_la_muerte.destruir_planeta(ilum)
    estrella_de_la_muerte.destruir_planeta(kamino)