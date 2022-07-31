import pygame as pg

class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        pass


class Portada(Escena):
    def bucle_principal(self):
     salir = False
     while not salir:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                salir = True
        self.pantalla.fill((99, 99, 99))
        pg.display.flip()


class Partidaone(Escena):
    def bucle_principal(self):
     salir = False
     while not salir:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                salir = True
        self.pantalla.fill((99, 99, 00))
        pg.display.flip()


class Partidatwo(Escena):
    def bucle_principal(self):
     salir = False
     while not salir:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                salir = True
        self.pantalla.fill((99, 00, 99))
        pg.display.flip()


class Records(Escena):
    def bucle_principal(self):
     salir = False
     while not salir:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                salir = True
        self.pantalla.fill((00, 99, 99))
        pg.display.flip()
