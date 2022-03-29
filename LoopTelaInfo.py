from pygame.constants import *
from Classes_Funcoes import *
from constantes import *
import pygame
import LoopJogo
from Extrair_metodo import *

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
        nome = mensagem("Olha o carteiro!", 35, cor_b)
        screen.blit(nome, (190, 50))
        
        # Mensagem "Escolha o jogador"
        msg1 = mensagem("Escolha um player:", 20, cor_v)
        screen.blit(msg1, (260, 240))

        # Mensagens das instruções na tela
        lista = aparece(m, t)
        i = 0
        for x in lista:
            screen.blit(x, (p[i], p[i+1]))
            i += 2

        # Imagens das duas opções
        carteira_sheet = pygame.image.load('Assets/Imagens/MailmanFemaleSpriteSheet.png').convert_alpha()
        carteira_sheet = carteira_sheet.subsurface((235, 0), (235, 336))
        carteira_sheet = pygame.transform.scale(carteira_sheet, (120, 170))
        screen.blit(carteira_sheet, (290, 280))
        carteiro_sheet = pygame.image.load('Assets/Imagens/MailmanSpriteSheet.png').convert_alpha()
        carteiro_sheet = carteiro_sheet.subsurface((235, 0), (235, 336))
        carteiro_sheet = pygame.transform.scale(carteiro_sheet, (120, 170))
        screen.blit(carteiro_sheet, (470, 280))

        pygame.display.flip()
    return state, player