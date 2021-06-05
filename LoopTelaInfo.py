from pygame.constants import *
from Classes import *
from constantes import *
from Funcoes import *
import pygame

def executar_tela_info (screen):
    # Música de inicio
    pygame.mixer.music.load("Som/Near_and_Far.ogg")
    pygame.mixer.music.set_volume(volume)
    clock = pygame.time.Clock()
    # Tela de fundo
    background = pygame.image.load('Imagens/8bitNY.jpg').convert()
    background = pygame.transform.scale(background, (largura, altura))
    background_rect = background.get_rect()

    correr = True

     # Música de fundo do jogo começa a tocar
    pygame.mixer.music.play(loops=-1)
    while correr:

        clock.tick(FramePerSecond)

        # Tratando os eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                state = MORTO
                correr = False
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    state = JOGAR
                    correr = False
                    # pygame.mixer.music.stop()

        # Atualizando a tela
        screen.blit(background, background_rect)

        pygame.display.flip()
    return state
