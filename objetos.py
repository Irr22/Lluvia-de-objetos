import pygame, random

class objeto(pygame.sprite.Sprite):
    def __init__(self,tipo):
        super().__init__()
        self.image = pygame.Surface([20, 20])

        if tipo == 'cura':
            self.image.fill((0,255,0)) # Verde
        elif tipo == 'daño':
            self.image.fill((255,0,0)) # Rojo
        elif tipo == 'monedas':
            self.image.fill((255,255,255)) # Blanco

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1,280)
        self.rect.y = 0
        self.velocidad = 2
        self.tipo = tipo

        self.ultima_vez_movida = 0
        self.mover_abajo = True

    def avanzar(self,tiempo_actual):
        if tiempo_actual - self.ultima_vez_movida > 4:
            if self.mover_abajo:
                self.rect.y += self.velocidad
                if self.rect.y <= 0:
                    self.mover_abajo = False
                self.ultima_vez_movida = tiempo_actual