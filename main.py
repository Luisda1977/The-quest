from the_quest import ANCHO, ALTO
from the_quest.game import the_quest

if __name__ == "__main__":
    print("Desde archivo main:")
    print(f"El tamaño de la pantalla es {ANCHO}x{ALTO}")
    juego = the_quest()
    juego.jugar()