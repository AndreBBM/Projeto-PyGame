# Importando e iniciando pacotes
from typing import Set
from pygame.constants import *
from random import *
from Classes import *
from constantes import *

import pygame
import random

pygame.init()

# Criando a tela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Olha o Carteiro!')


#Exibir mensagens:
def mensagem(msg,tamanho,cor):
    fonte=pygame.font.SysFont("comicsansms",tamanho,True,False) #Penultimo:Negrito Último:Italico
    mensagem= f"{msg}" #F--F string--- Mesma coisa que .format
    texto_formatado=fonte.render(mensagem,True, cor) #Textocerrilhado- Segundo
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

todas_as_sprites = pygame.sprite.Group()
carteiro_andando = Carteiro(carteiro_sheet)
todas_as_sprites.add(carteiro_andando)

# Grupo colisão com a carteira
grupo_obstaculo = pygame.sprite.Group()

obstaculo = None
obstaculo_invisivel = None

# São criados 2 fundos, um incial e outro logo após o primeiro, que aparece quando o primeiro sai da tela
bg_e = 0
bg_d = background.get_width()

# Iniciando a estrutura 
Start = True

# Rodando o cenário
clock = pygame.time.Clock()
FramePerSecond = 100
velocidade_tela = 2.4

#Reiniciar
def reiniciar_jogo():
    velocidade_tela=2.4
    colisoes=False


# Loop Principal!
while Start:
    clock.tick(FramePerSecond)
    # Tratando eventos
    for event in pygame.event.get():
        # Para sair do jogo
        if event.type == QUIT:
            Start = False
        # Para pular
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if carteiro_andando.rect.y != carteiro_andando.inicial_y:
                    pass
                else:
                    carteiro_andando.pula()
            if event.key==K_SPACE and colisoes:
                reiniciar_jogo()

    # Velocidade com que o fundo se mexe
    bg_e -= velocidade_tela
    bg_d -= velocidade_tela

    # Quando os fundos saem completamente da tela, eles voltam para o início para passarem novamente
    if bg_e < background.get_width() * -1:
        bg_e = background.get_width()

    if bg_d < background.get_width() * -1:
        bg_d = background.get_width()

    if obstaculo == None or obstaculo.rect.x < (largura - 400):
        opcao = random.randint(1, 2)
        if opcao == 1:
            obstaculo = Cone(cone_img)
            
            
        if opcao == 2:
            referencia= Poste(poste_img)
            obstaculo = Quadrado(poste_img,referencia)
            todas_as_sprites.add(referencia)

        todas_as_sprites.add(obstaculo)
        grupo_obstaculo.add(obstaculo)        

    colisoes = pygame.sprite.spritecollide(carteiro_andando, grupo_obstaculo, False, pygame.sprite.collide_mask)

    # Linhas importantes = Fazem o jogo ficar sempre se atualizando
    tela.blit(background, (bg_e, -270))
    tela.blit(background, (bg_d, -270))
    todas_as_sprites.draw(tela)

    # Caso colida com algum dos obstáculos, o fundo para de andar
    if colisoes:
        velocidade_tela = 0
        cabou= mensagem("ENCOMENDAS NÃO ENTREGUES :(",30,(255,0,255))
        tela.blit(cabou,(300,200))
        restart=mensagem("Pressione espaço para reiniciar!",25,(255,0,255))
        tela.blit(restart,(350,280))

    else:
        todas_as_sprites.update()
        grupo_obstaculo.update()

    pygame.display.update()

# Encerrando o PyGame
pygame.quit()