import os

import pygame as pg

from . import ANCHO, ALTO

class Escena:
    def __init__(self, pantalla: pg.Surface):
        self.pantalla = pantalla

    def bucle_principal(self):
        pass


class Portada(Escena):
    def __init__(self, pantalla: pg.Surface):
       super().__init__(pantalla)  

    def bucle_principal(self):
     salir = False
     while not salir:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                salir = True
        self.pantalla.fill((99, 99, 99))
        self.pintar_titulo()
        pg.display.flip()

    def pintar_titulo(self):
        pos_x = 


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
