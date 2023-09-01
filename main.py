import pygame, sys

pygame.init()

ANCHO = 1280
LARGO = 720

size = (ANCHO, LARGO)

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        print(event)
        #Cierre del juego
        if event.type == pygame.QUIT:
            sys.exit()