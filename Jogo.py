# Importando e iniciando pacotes
from typing import Set
from pygame.constants import *
from random import *
from Classes import *
from constantes import *
import pygame
import random
import os
pygame.init()
pygame.mixer.init()

# Criando a tela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Olha o Carteiro!')

# Exibir mensagens:
def mensagem(msg, tamanho, cor):
    fonte = pygame.font.Font('font/PressStart2P.ttf', tamanho)
    mensagem = f"{msg}"  # F--F string--- Mesma coisa que .format
    texto_formatado = fonte.render(mensagem, True, cor)  # Textocerrilhado- Segundo
    return texto_formatado

# Carregando imagens:
background = pygame.image.load('Imagens/8bitNY.jpg').convert()  # Não precisa de transparência aqui
background = pygame.transform.scale(background, (1000, 800))
carteiro_sheet = pygame.image.load('Imagens/MailmanFemaleSpriteSheet.png').convert_alpha()
carteiro_img = pygame.image.load('Imagens/MailmanFemale.png').convert_alpha()
carteiro_img = pygame.transform.scale(carteiro_img, (WIDTH_cart, HEIGHT_cart))
poste_img = pygame.image.load('Imagens/poste.png').convert_alpha()
poste_img = pygame.transform.scale(poste_img, (WIDTH_pole, HEIGHT_pole))
caixas_img = pygame.image.load('Imagens/Caixa.png').convert_alpha()
caixas_img = pygame.transform.scale(caixas_img, (WIDTH_caixa, HEIGHT_caixa))
cone_img = pygame.image.load('Imagens/cone.png').convert_alpha()
cone_img = pygame.transform.scale(cone_img, (WIDTH_cone, HEIGHT_cone))

# Carregando sons:
som_do_pulo = pygame.mixer.Sound('Som/mb_jump.wav')


def iniciando(screen):
    clock = pygame.time.Clock()
    background = pygame.image.load('Imagens/8bitNY.jpg').convert()
    background = pygame.transform.scale(background, (1000, 800))
    background_rect = background.get_rect()
    correr = True
    while correr:
        clock.tick(FramePerSecond)
        for event in pygame.event.get():
            if event.type == QUIT:
                state = DESISTINDO
                correr = False
            if event.type == KEYUP:
                state = JOGANDO
                correr = False
        screen.blit(background, background_rect)
        pygame.display.flip()
    return state


def joguinho(tela):
    # Rodando o cenário
    clock = pygame.time.Clock()
    
    todas_as_sprites = pygame.sprite.Group()
    carteiro_andando = Carteiro(carteiro_sheet)
    todas_as_sprites.add(carteiro_andando)
    # Grupo colisão com a carteira
    grupo_obstaculo = pygame.sprite.Group()
    
    ACABOU = 0
    JOGAR = 1
    MORTO = 2
    state = JOGAR

    obstaculo = None
    obstaculo_invisivel = None

    # São criados 2 fundos, um incial e outro logo após o primeiro, que aparece quando o primeiro sai da tela
    bg_e = 0
    bg_d = background.get_width()
    
    #pygame.mixer.music.play(loops=-1)    
    # Loop Principal!
    while state != ACABOU:
        clock.tick(FramePerSecond)
        # Tratando eventos
        for event in pygame.event.get():
            # Para sair do jogo
            if event.type == QUIT:
                state = ACABOU
                exit()
            # Estando no jogo
            if state == JOGAR:
                # Para pular
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        if carteiro_andando.rect.y != carteiro_andando.inicial_y:
                            pass
                        else:
                            carteiro_andando.pula()
            if state == MORTO:
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                            todas_as_sprites.empty()
                            todas_as_sprites.add(carteiro_andando)
                            grupo_obstaculo.empty()
                            state = JOGAR
                            colisoes.clear()
                            obstaculo = None
                    elif event.key == QUIT or event.key == K_q:
                        state = DESISTINDO

        if obstaculo == None or obstaculo.rect.x < (largura - 400):
            opcao = random.randint(1, 2)
            if opcao == 1:
                obstaculo = Cone(cone_img)

            if opcao == 2:
                referencia = Poste(poste_img)
                obstaculo = Quadrado(poste_img, referencia)
                todas_as_sprites.add(referencia)

            todas_as_sprites.add(obstaculo)
            grupo_obstaculo.add(obstaculo)
            
        if state == MORTO:
            velocidade_tela = 0            
        else:
            velocidade_tela = 2.4
            todas_as_sprites.update()
        colisoes = pygame.sprite.spritecollide(carteiro_andando, grupo_obstaculo, False, pygame.sprite.collide_mask)

        if len(colisoes) > 0:
            state = MORTO
        
        # Velocidade com que o fundo se mexe
        bg_e -= velocidade_tela
        bg_d -= velocidade_tela

        # Quando os fundos saem completamente da tela, eles voltam para o início para passarem novamente
        if bg_e < background.get_width() * -1:
            bg_e = background.get_width()

        if bg_d < background.get_width() * -1:
            bg_d = background.get_width()

        # Linhas importantes = Fazem o jogo ficar sempre se atualizando
        tela.blit(background, (bg_e, -270))
        tela.blit(background, (bg_d, -270))

        if state == MORTO:
            cabou = mensagem("ENCOMENDAS NÃO ENTREGUES :(", 30, (255, 255, 0))
            tela.blit(cabou, (70, 100))
            restart = mensagem("Pressione espaço para reiniciar!", 25, (255, 255, 0))
            tela.blit(restart, (70, 180))
        # Caso colida com algum dos obstáculos, o fundo para de andar
        todas_as_sprites.draw(tela)
        pygame.display.update()
    return state

state = INICIANDO
while state != DESISTINDO:
    if state == INICIANDO:
        state = iniciando(tela)
    elif state == JOGANDO:
        state = joguinho(tela)
    else:
        state = DESISTINDO
# Encerrando o PyGame
pygame.quit()
