import pygame
from pygame.constants import *
from constantes import *


# Exibir mensagens:
def mensagem(msg, tamanho, cor):
    fonte = pygame.font.Font('font/PressStart2P.ttf', tamanho)
    mensagem = f"{msg}"  # F--F string--- Mesma coisa que .format
    texto_formatado = fonte.render(mensagem, True, cor)  # Textocerrilhado- Segundo
    return texto_formatado

def iniciando(screen):
    clock = pygame.time.Clock()
    background = pygame.image.load('Imagens/8bitNY.jpg').convert()
    background = pygame.transform.scale(background, (largura, altura))
    background_rect = background.get_rect()
    correr = True
    while correr:
        clock.tick(FramePerSecond)
        for event in pygame.event.get():
            if event.type == QUIT:
                state = MORTO
                correr = False
            if event.type == KEYUP:
                state = JOGAR
                correr = False
        screen.blit(background, background_rect)
        pygame.display.flip()
    return state
