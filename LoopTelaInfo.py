from pygame.constants import *
from Classes import *
from constantes import *
from Funcoes import *
import pygame

def executar_tela_info (screen):
    # Música de inicio
    pygame.mixer.music.load("Assets/Som/Near_and_Far.ogg")
    pygame.mixer.music.set_volume(volume)
    clock = pygame.time.Clock()
    # Tela de fundo
    background = pygame.image.load('Assets/Imagens/carta.jpg').convert()
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
        # Imagem de fundo: carta
        screen.blit(background, background_rect)

        # Nome do jogo
        nome = mensagem("Olha o carteiro!", 35, (0, 0, 0))
        screen.blit(nome, (190, 50))

        # Mensagem com o objetivo do jogo
        objetivo1 = mensagem("Objetivo do", 30, (0, 0, 0))
        screen.blit(objetivo1, (70, 295))
        objetivo2 = mensagem("jogo:", 30, (0, 0, 0))
        screen.blit(objetivo2, (165, 335))
        objetivo3 = mensagem("Desviar dos cones", 20, (0, 0, 0))
        screen.blit(objetivo3, (70, 375))
        objetivo4 = mensagem("e das lâmpadas", 20, (0, 0, 0))
        screen.blit(objetivo4, (100, 405))
        objetivo4 = mensagem("dos postes.", 20, (0, 0, 0))
        screen.blit(objetivo4, (130, 435))

        # Mensagem sobre como jogar
        instrucoes1 = mensagem("Como jogar?", 30, (0, 0, 0))
        screen.blit(instrucoes1, (520, 300))
        instrucoes2 = mensagem("Para pular", 20, (0, 0, 0))
        screen.blit(instrucoes2, (590, 340))
        instrucoes3 = mensagem("pressione", 20, (0, 0, 0))
        screen.blit(instrucoes3, (595, 370))
        instrucoes4 = mensagem("a setinha", 20, (0, 0, 0))
        screen.blit(instrucoes4, (595, 400))
        instrucoes4 = mensagem("para cima.", 20, (0, 0, 0))
        screen.blit(instrucoes4, (595, 430))

        pygame.display.flip()
    return state
