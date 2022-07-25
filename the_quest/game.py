import pygame

from the_quest import ALTO, ANCHO

class the_quest:
    def __init__(self) -> None:
        print("Comienza el juego")
        pygame.init()
        self.display = pygame.display.set_mode((ANCHO, ALTO))

    def jugar(self):
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir = True
            self.display.fill((99, 99, 99))
            pygame.display.flip()

