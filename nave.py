import pygame

class Nave:
    def __init__(self):
        self.nave_ancho = 50
        self.nave_alto = 30
        self.nave_color = (255, 255, 255)
        self.nave_x = 50
        self.nave_y = 300

    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and self.nave_y > 0:
            self.nave_y -= 5
        elif teclas[pygame.K_DOWN] and self.nave_y < 600 - self.nave_alto:
            self.nave_y += 5

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.nave_color, (self.nave_x, self.nave_y, self.nave_ancho, self.nave_alto))

