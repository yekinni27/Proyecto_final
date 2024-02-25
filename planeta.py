import pygame

class Planeta:
    def __init__(self):
        self.planeta_imagen = pygame.image.load("planeta.png")
        self.planeta_imagen = pygame.transform.scale(self.planeta_imagen, (100, 100))
        self.planeta_x = 700
        self.planeta_y = 250

    def dibujar(self, pantalla):
        pantalla.blit(self.planeta_imagen, (self.planeta_x, self.planeta_y))
