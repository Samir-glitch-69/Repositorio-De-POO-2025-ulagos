import pygame
import random
from settings import RED, BLUE, SCREEN_WIDTH, SCREEN_HEIGHT, METEOR_SPEED

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Crear una superficie para el meteorito
        radius = random.randint(10, 30)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        
        # Dibujar un círculo rojo
        pygame.draw.circle(self.image, RED, (radius, radius), radius)
        
        # Obtener el rectángulo de la imagen
        self.rect = self.image.get_rect()
        
        # Posición inicial aleatoria en la parte superior
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        
        # Velocidad del meteorito
        self.speed = METEOR_SPEED
        
    def update(self):
        # Mover el meteorito hacia abajo
        self.rect.y += self.speed
        
        # Eliminar si sale de la pantalla
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


class FastMeteor(Meteor):
    def __init__(self):
        super().__init__()
        # Cambiar color a azul
        radius = self.rect.width // 2
        self.image.fill((0, 0, 0, 0))  # Limpiar la superficie
        pygame.draw.circle(self.image, BLUE, (radius, radius), radius)
        
        # Velocidad doble
        self.speed = METEOR_SPEED * 2