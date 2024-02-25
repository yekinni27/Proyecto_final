import pygame
from nave import Nave
from planeta import Planeta

class Juego:
    def __init__(self):
        pygame.display.set_caption("Juego Pygame")
        self.pantalla = pygame.display.set_mode((800, 600))
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 36)
        self.sonido_explosion = pygame.mixer.Sound("explosion.wav")
        self.cargar_musica_fondo("background_music.mp3")
        self.nave = Nave()
        self.planeta = Planeta()
        self.fondo_galaxia = pygame.image.load("galaxia.jpg").convert()
        self.fondo_galaxia = pygame.transform.scale(self.fondo_galaxia, (800, 600))

    def cargar_musica_fondo(self, archivo_musica):
        pygame.mixer.music.load(archivo_musica)

    def reproducir_musica_fondo(self, repeticiones=-1):
        pygame.mixer.music.play(repeticiones)

    def detener_musica_fondo(self):
        pygame.mixer.music.stop()

    def iniciar(self):
        self.reproducir_musica_fondo()

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.detener_musica_fondo()
                    pygame.quit()
                    quit()

            self.pantalla.blit(self.fondo_galaxia, (0, 0))

            # Resto de la lógica del juego...
            self.nave.mover()
            self.nave.dibujar(self.pantalla)
            self.planeta.dibujar(self.pantalla)

            pygame.display.flip()
            self.reloj.tick(60)
