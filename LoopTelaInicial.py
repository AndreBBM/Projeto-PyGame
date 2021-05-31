from pygame.constants import *
from Classes import *
from Constantes import *
import pygame

def executar(screen):
    clock = pygame.time.Clock()
    background = pygame.image.load('Imagens/8bitNY.jpg').convert()
    background = pygame.transform.scale(background, (1000, 800))
    background_rect = background.get_rect()
    correr = True
    while correr:
        clock.tick(FramePerSecond)
        for event in pygame.event.get():
            if event.type == QUIT:
                state = DESISTINDO
                correr = False
            if event.type == KEYUP:
                state = JOGANDO
                correr = False
        screen.blit(background, background_rect)
        pygame.display.flip()
    return state
