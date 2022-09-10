import os

import pygame as pg
from pygame.sprite import Sprite

from the_quest import ALTO, ANCHO


class Cohete(Sprite):

    def __init__(self) -> None:
        super().__init__()
        image_path = os.path.join("resources", "imagenes", "fighterspr1c.png")
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(center=(ANCHO-900, ALTO-300))

    def update(self) -> None:
        return super().update()
