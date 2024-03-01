import pygame

class cesta(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([50,30])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = 1
        self.ultima_pulsacion_spacio = 0

        self.monedas = 0
        self.vida = 3

        self.tipo = 'cesta'

    def movement(self,key,tiempo_actual):
        if tiempo_actual - self.ultima_pulsacion_spacio >= 2: 
            if key[pygame.K_d] and self.rect.x < 290 - 50:
                self.rect.x += self.velocidad
            elif key[pygame.K_a] and self.rect.x > 10:
                self.rect.x -= self.velocidad
            self.ultima_pulsacion_spacio = tiempo_actual
        