from pygame.constants import *
from Classes import *
from constantes import *
import pygame

# Função de tela inicial
def executar_tela_inicial(screen):
    clock = pygame.time.Clock()
    # Tela de fundo
    background = pygame.image.load('Imagens/8bitNY.jpg').convert()
    background = pygame.transform.scale(background, (largura, altura))
    background_rect = background.get_rect()
    correr = True
    # Enquanto a tela correr
    while correr:
        clock.tick(FramePerSecond)
        # Tratando os eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                state = MORTO
                correr = False
            if event.type == KEYUP:
                state = JOGAR
                correr = False
        # Atualizando a tela
        screen.blit(background, background_rect)
        pygame.display.flip()
    return state
