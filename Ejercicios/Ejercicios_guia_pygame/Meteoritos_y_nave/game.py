import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, RED, METEOR_FREQUENCY
from player import Player
from meteor import Meteor, FastMeteor

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Nave Espacial vs Meteoritos")
        self.clock = pygame.time.Clock()
        
        # Grupos de sprites
        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()
        
        # Crear jugador
        self.player = Player()
        self.all_sprites.add(self.player)
        
        # Estado del juego
        self.running = True
        self.score = 0
        
    def run(self):
        # Bucle principal del juego
        while self.running:
            # Mantener el juego a 60 FPS
            dt = self.clock.tick(60) / 1000.0
            
            # 1. Procesar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # 2. Generar meteoritos aleatoriamente
            if random.randint(1, 100) <= METEOR_FREQUENCY:
                # 80% meteorito normal, 20% meteorito rápido
                if random.random() < 0.8:
                    meteor = Meteor()
                else:
                    meteor = FastMeteor()
                
                self.all_sprites.add(meteor)
                self.meteors.add(meteor)
            
            # 3. Actualizar todos los sprites
            self.all_sprites.update()
            
            # 4. Detectar colisiones
            hits = pygame.sprite.spritecollide(self.player, self.meteors, False)
            if hits:
                self.running = False
            
            # 5. Dibujar / renderizar
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            
            # Mostrar puntaje
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Puntaje: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            
            # Incrementar puntaje
            self.score += 1
            
            # 6. Voltear la pantalla
            pygame.display.flip()
        
        # Mostrar mensaje de Game Over
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.screen.blit(game_over_text, text_rect)
        pygame.display.flip()
        
        # Esperar un momento antes de cerrar
        pygame.time.wait(2000)