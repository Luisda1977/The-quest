import pygame as pg

from the_quest import ALTO, ANCHO

class the_quest:
    def __init__(self) -> None:
        print("Comienza el juego")
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO))

    def jugar(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.display.fill((99, 99, 99))
            pg.display.flip()

