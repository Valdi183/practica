from EstrellaDeLaMuerte import EstrellaDeLaMuerte
from Planetas import PlanetaConcordia, PlanetaIlum, PlanetaKamino
from Naves import NavePequeña, NaveGrande

if __name__ == "__main__":
    estrella_de_la_muerte = EstrellaDeLaMuerte()
    
    # Crear instancias de planetas
    concordia = PlanetaConcordia()
    ilum = PlanetaIlum()
    kamino = PlanetaKamino()
    
    # Destruir planetas
    estrella_de_la_muerte.destruir_planeta(concordia)
    estrella_de_la_muerte.destruir_planeta(ilum)
    estrella_de_la_muerte.destruir_planeta(kamino)
    
    # Crear instancias de naves aliadas
    nave_pequeña = NavePequeña("Nave Pequeña Alpha")
    nave_grande = NaveGrande("Nave Grande Omega")
    
    # Atacar naves aliadas
    estrella_de_la_muerte.atacar_nave(nave_pequeña)
    estrella_de_la_muerte.atacar_nave(nave_grande)