from pygame.constants import *
from Classes_Funcoes import *
from constantes import *
import pygame
import LoopJogo


# Função da segunda tela
def executar_tela_info(screen):
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
    player = 0
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
                # Escolhe jogador
                if event.key == K_o:
                    state= JOGAR
                    correr = False
                    player = 1
                if event.key == K_a:
                    state= JOGAR
                    correr = False
                    player = 0
                # Ao escolher o player, muda-se a tela de forma automática
        
        # Atualizando a tela
        # Imagem de fundo: carta
        screen.blit(background, background_rect)
        # Nome do jogo
        nome = mensagem("Olha o carteiro!", 35, (0, 0, 0))
        screen.blit(nome, (190, 50))
        # Mensagem com o objetivo do jogo
        objetivo1 = mensagem("Objetivo", 20, (0, 0, 0))
        screen.blit(objetivo1, (60, 260))
        objetivo2 = mensagem("do jogo:", 20, (0, 0, 0))
        screen.blit(objetivo2, (65, 280))
        objetivo3 = mensagem("Desviar dos", 15, (0, 0, 0))
        screen.blit(objetivo3, (60, 330))
        objetivo4 = mensagem("cones e das", 15, (0, 0, 0))
        screen.blit(objetivo4, (60, 350))
        objetivo5 = mensagem("lâmpadas", 15, (0, 0, 0))
        screen.blit(objetivo5, (80, 370))
        objetivo6 = mensagem("dos postes.", 15, (0, 0, 0))
        screen.blit(objetivo6, (60, 390))

        # Mensagem sobre o player
        msg1 = mensagem("Escolha um player:", 20, (255, 0, 0))
        screen.blit(msg1, (260, 240))
        msg2 = mensagem("Carteira", 15, (0, 0, 0))
        screen.blit(msg2, (280, 270))
        msg3 = mensagem("Carteiro", 15, (0, 0, 0))
        screen.blit(msg3, (460, 270))
        msg4 = mensagem("Tecla A", 15, (0, 0, 0))
        screen.blit(msg4, (290, 450))
        msg5 = mensagem("Tecla O", 15, (0, 0, 0))
        screen.blit(msg5, (470, 450))

        # Imagens das duas opções
        carteira_sheet = pygame.image.load('Assets/Imagens/MailmanFemaleSpriteSheet.png').convert_alpha()
        carteira_sheet = carteira_sheet.subsurface((235, 0), (235, 336))
        carteira_sheet = pygame.transform.scale(carteira_sheet, (120, 170))
        screen.blit(carteira_sheet, (290, 280))
        carteiro_sheet = pygame.image.load('Assets/Imagens/MailmanSpriteSheet.png').convert_alpha()
        carteiro_sheet = carteiro_sheet.subsurface((235, 0), (235, 336))
        carteiro_sheet = pygame.transform.scale(carteiro_sheet, (120, 170))
        screen.blit(carteiro_sheet, (470, 280))

        # Mensagem sobre como jogar
        instrucoes1 = mensagem("Como jogar?", 20, (0, 0, 0))
        screen.blit(instrucoes1, (630, 265))
        instrucoes2 = mensagem("Para pular", 15, (0, 0, 0))
        screen.blit(instrucoes2, (670, 320))
        instrucoes3 = mensagem("pressione", 15, (0, 0, 0))
        screen.blit(instrucoes3, (675, 340))
        instrucoes4 = mensagem("a setinha", 15, (0, 0, 0))
        screen.blit(instrucoes4, (675, 360))
        instrucoes4 = mensagem("para cima.", 15, (0, 0, 0))
        screen.blit(instrucoes4, (670, 380))

        pygame.display.flip()
    return state, player
