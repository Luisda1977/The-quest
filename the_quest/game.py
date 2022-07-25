import pygame

from the_quest import ALTO, ANCHO

class the_quest:
    def __init__(self) -> None:
        print("Comienza el juego")
        pygame.init()
        pygame.display.set_mode((ANCHO, ALTO))

if __name__ == "__main__":
    the_quest()