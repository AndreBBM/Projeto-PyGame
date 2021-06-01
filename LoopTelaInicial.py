from pygame.constants import *
from Classes import *
from constantes import *
from Funcoes import *
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
        nome = mensagem("Olha o carteiro!", 35, (255, 255, 0))
        screen.blit(nome, (190, 50))
        comecar = mensagem("Pressione espaço para continuar", 20, (255, 255, 0))
        screen.blit(comecar, (150, 450))
        pygame.display.flip()
    return state
