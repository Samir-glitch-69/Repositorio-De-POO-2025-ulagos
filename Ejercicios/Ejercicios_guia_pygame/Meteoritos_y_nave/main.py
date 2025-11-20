import pygame
from game import Game

if __name__ == "__main__":
    # Crear una instancia del juego
    game = Game()
    
    # Iniciar el bucle principal del juego
    game.run()
    
    # Salir de Pygame
    pygame.quit()