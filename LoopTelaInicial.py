from pygame.constants import *
from Classes import *
from constantes import *
from Funcoes import *
import pygame


# Função de tela inicial
def executar_tela_inicial(screen):
    # Música de inicio
    pygame.mixer.music.load("Som/Near_and_Far.ogg")
    pygame.mixer.music.set_volume(volume)
    clock = pygame.time.Clock()
    # Tela de fundo
    background = pygame.image.load('Imagens/8bitNY.jpg').convert()
    background = pygame.transform.scale(background, (largura, altura))
    background_rect = background.get_rect()
    carteiro_img = pygame.image.load('Imagens/MailmanFemale.png').convert_alpha()
    carteiro_img = pygame.transform.scale(carteiro_img, (230, 300))
    caixa_correio = pygame.image.load('Imagens/Caixa_de_correio.png').convert_alpha()
    caixa_correio = pygame.transform.scale(caixa_correio, (430, 450))

    correr = True
    # Música de fundo do jogo começa a tocar
    pygame.mixer.music.play(loops=-1)

    # Enquanto a tela correr
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
        screen.blit(carteiro_img, (100, 150))
        screen.blit(caixa_correio, (150, 110))
        nome = mensagem("Olha o carteiro!", 35, (255, 255, 0))
        screen.blit(nome, (190, 50))
        como_jogar = mensagem("COMO JOGAR?", 30, (255, 255, 0))
        screen.blit(como_jogar, (510, 300))
        instrucoes1 = mensagem("Desvie dos obstáculos.", 20, (255, 255, 0))
        screen.blit(instrucoes1, (450, 340))
        instrucoes2 = mensagem("Para pular pressione a", 20, (255, 255, 0))
        screen.blit(instrucoes2, (450, 365))
        instrucoes3 = mensagem("setinha para cima.", 20, (255, 255, 0))
        screen.blit(instrucoes3, (500, 390))
        comecar = mensagem("Pressione espaço para continuar", 20, (255, 255, 0))
        screen.blit(comecar, (150, 470))

        pygame.display.flip()
    return state
