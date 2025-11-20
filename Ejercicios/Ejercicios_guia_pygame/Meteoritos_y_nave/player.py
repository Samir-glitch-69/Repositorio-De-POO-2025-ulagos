import pygame
from settings import GREEN, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Crear una superficie transparente para el triángulo
        self.image = pygame.Surface((40, 50), pygame.SRCALPHA)  # Más alto que ancho para forma de nave
        
        # Dibujar un triángulo estilizado (forma de nave espacial)
        points = [
            (20, 0),    # Punta superior (centro)
            (0, 50),    # Esquina inferior izquierda
            (40, 50)    # Esquina inferior derecha
        ]
        pygame.draw.polygon(self.image, GREEN, points)
        
        # Añadir detalles al triángulo
        pygame.draw.polygon(self.image, (100, 255, 100), [(15, 10), (25, 10), (20, 20)])  # Ventana
        pygame.draw.line(self.image, (150, 255, 150), (10, 40), (30, 40), 2)  # Línea decorativa
        
        # Obtener el rectángulo de la imagen
        self.rect = self.image.get_rect()
        
        # Posicionar la nave en la parte inferior central
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        
        # Velocidad del jugador
        self.speed = PLAYER_SPEED
        
    def update(self):
        # Obtener el estado de las teclas
        keys = pygame.key.get_pressed()
        
        # Movimiento horizontal
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            
        # Mantener al jugador dentro de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH