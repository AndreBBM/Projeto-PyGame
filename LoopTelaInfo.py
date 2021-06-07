from pygame.constants import *
from Classes import *
from constantes import *
from Funcoes import *
import pygame

# Função da segunda tela
def executar_tela_info (screen):
    # Tela de fundo
    background = pygame.image.load('Assets/Imagens/carta.jpg').convert()
    background = pygame.transform.scale(background, (largura, altura))
    background_rect = background.get_rect()
    # Rodando o cenário
    clock = pygame.time.Clock()
    # Música de inicio
    pygame.mixer.music.load("Assets/Som/GuineaPigHero.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=-1)

    correr = True
    # Enquanto a tela correr
    while correr:
        clock.tick(FramePerSecond)
        # Tratando os eventos
        for event in pygame.event.get():
            # Sair
            if event.type == QUIT:
                state = MORTO
                correr = False
            # Se uma tecla for tocada
            if event.type == KEYUP:
                # Se a tecla for espaço
                if event.key == K_SPACE:
                    state = JOGAR
                    correr = False

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
