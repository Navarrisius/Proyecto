import pygame
from random import randint

def generar_mountain(screen, x_pos, y_pos):
    cont = 0
    color = (150, 150, 150)
    while cont < randint(30, 120):
        altura = randint(-5, -1)
        pygame.draw.line(screen, color, (x_pos, y_pos), (x_pos, y_pos + altura), 2)
        x_pos += randint(1, 2)
        y_pos += altura
        cont += 1
    cont = 0
    while cont < randint(20, 40):
        altura = randint(-1, 1)
        pygame.draw.line(screen, color, (x_pos, y_pos), (x_pos, y_pos + altura), 2)
        x_pos += randint(1, 3)
        y_pos += altura
        cont += 1
    cont = 0
    while cont < randint(30, 120):
        altura = randint(1, 5)
        pygame.draw.line(screen, color, (x_pos, y_pos), (x_pos, y_pos + altura), 2)
        x_pos += randint(1, 2)
        y_pos += altura
        cont += 1
    return [x_pos, y_pos]
    

def generar_terreno(screen, largo, ancho):
    color = (50, 50, 50)
    x_pos = 0
    y_pos = ancho - ancho / 6
    pos_random1 = randint(0, largo / 5)
    while x_pos < largo:
        if x_pos == pos_random1:
            pos = generar_mountain(screen, x_pos, y_pos)
            x_pos = pos[0]
            y_pos = pos[1]
        altura = randint(-2, 2)
        pygame.draw.line(screen, color, (x_pos, y_pos), (x_pos, y_pos + altura), 2)
        x_pos += randint(1, 2)
        y_pos += altura