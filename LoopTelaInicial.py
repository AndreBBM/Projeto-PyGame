from pygame.constants import *
from Classes import *
from constantes import *
from Funcoes import *
import pygame


# Função de tela inicial
def executar_tela_inicial(screen):
    # Tela de fundo
    background = pygame.image.load('Assets/Imagens/8bitNY.jpg').convert()
    background = pygame.transform.scale(background, (largura, altura))
    background_rect = background.get_rect()
    carteiro_img = pygame.image.load('Assets/Imagens/carteira_nova.png').convert_alpha()
    carteiro_img = pygame.transform.scale(carteiro_img, (230, 300))
    caixa_correio = pygame.image.load('Assets/Imagens/Caixa_de_correio.png').convert_alpha()
    caixa_correio = pygame.transform.scale(caixa_correio, (430, 450))
    # Rodando o cenário
    clock = pygame.time.Clock()
    # Música de inicio
    pygame.mixer.music.load("Assets/Som/Near_and_Far.ogg")
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
                    state = INFO
                    correr = False

        # Atualizando a tela
        screen.blit(background, background_rect)
        screen.blit(carteiro_img, (280, 150))
        screen.blit(caixa_correio, (330, 110))
        nome = mensagem("Olha o carteiro!", 35, (255, 255, 0))
        screen.blit(nome, (180, 50))
        comecar = mensagem("Pressione espaço para continuar", 20, (255, 255, 0))
        screen.blit(comecar, (150, 470))

        pygame.display.flip()
    return state
