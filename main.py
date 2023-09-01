import pygame
from funciones.generar_terreno import generar_terreno

pygame.init()
LARGO = 1280
ANCHO = 720
screen = pygame.display.set_mode((LARGO, ANCHO))
clock = pygame.time.Clock()
running = True
generar_terreno(screen, LARGO, ANCHO)
while running:
    
    # Cierre del juego
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    
    clock.tick(60)  # limits FPS to 60

pygame.quit()