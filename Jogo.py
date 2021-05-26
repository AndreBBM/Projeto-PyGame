# Importando e iniciando pacotes
from typing import Set
import pygame
from pygame.constants import *
from random import *
from Classes import *
import Setup
import random

config = Setup.LoadConfig()
pygame.init()

# Criando a tela do jogo
# Dimensões da tela
altura = 500
largura = 900
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Olha o Carteiro!')

# Dimensões das imagens colocadas
WIDTH_cart = 50
WIDTH_pole = 100
WIDTH_cone = 50
WIDTH_caixa = 50

HEIGHT_cart = 50
HEIGHT_pole = 200
HEIGHT_cone = 50
HEIGHT_caixa = 50

# Posição inicial do carteiro
carteiro_y = 420
carteiro_x = 150

# Carregando imagens: somente estruturando
background = pygame.image.load('Imagens/8bitNY.jpg').convert()  # Não precisa de transparência aqui
background = pygame.transform.scale(background, (1000, 800))
carteiro_sheet = pygame.image.load('Imagens/MailmanFemaleSpriteSheet.png').convert_alpha()
carteiro_img = pygame.image.load('Imagens/MailmanFemale.png').convert_alpha()
carteiro_img = pygame.transform.scale(carteiro_img, (WIDTH_cart, HEIGHT_cart))
poste_img = pygame.image.load('Imagens/poste.png').convert_alpha()
poste_img = pygame.transform.scale(poste_img, (WIDTH_pole, HEIGHT_pole))
caixas_img = pygame.image.load('Imagens/Caixa.jpg').convert_alpha()
caixas_img = pygame.transform.scale(caixas_img, (WIDTH_caixa, HEIGHT_caixa))
cone_img = pygame.image.load('Imagens/cone.png').convert_alpha()
cone_img = pygame.transform.scale(cone_img, (WIDTH_cone, HEIGHT_cone))


# Testando sprite - Carteiro
class Carteiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Faces da carteira e dimensionando escala
        self.img1 = carteiro_sheet.subsurface((0, 0), (235, 336))
        self.img1 = pygame.transform.scale(self.img1, (235 - 170, 336 - 250))
        self.img2 = carteiro_sheet.subsurface((0, 336), (235, 336))
        self.img2 = pygame.transform.scale(self.img2, (235 - 170, 336 - 250))
        self.img3 = carteiro_sheet.subsurface((235, 0), (235, 336))
        self.img3 = pygame.transform.scale(self.img3, (235 - 170, 336 - 250))
        self.imagens = [self.img1, self.img2, self.img3]
        self.index_lista = 0
        self.image = self.imagens[self.index_lista]
        self.rect = self.image.get_rect()
        # Criando máscara da sprite
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.center = (carteiro_x, carteiro_y)
        self.inicial_y = carteiro_y - 250 // 4
        self.pular = False

    def pula(self):
        self.pular = True

    def update(self):
        if self.pular == True:
            if self.rect.y <= 150:
                self.pular = False
            self.rect.y -= 10
        if self.index_lista > 2:
            self.index_lista = 0
        else:
            if self.rect.y < self.inicial_y:
                self.rect.y += 5
            else:
                self.rect.y = self.inicial_y

        self.index_lista += 0.25
        self.image = self.imagens[int(self.index_lista)]


class Quadrado(pygame.sprite.Sprite):
    def __init__(self, poste):
        pygame.sprite.Sprite.__init__(self)
        self.image = caixas_img
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        # Criando máscara da sprite
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (300, 150)
        self.referencia_poste = poste

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.centerx = self.referencia_poste.rect.centerx
        self.rect.x -= 4


todas_as_sprites = pygame.sprite.Group()
colisoes_com_carteiro = pygame.sprite.Group()
carteiro_andando = Carteiro()
poste = Poste(poste_img)
quadrado = Quadrado(poste)
'''
cone = Cone(cone_img)
colisoes_com_carteiro.add(cone)
poste = Poste(poste_img)
quadrado = Quadrado(poste)
caixa = Caixa(caixas_img)
todas_as_sprites.add(poste)
todas_as_sprites.add(cone)
todas_as_sprites.add(caixa)
'''
# todas_as_sprites.add(quadrado)-- Ele tá lá, mas não desenhado
todas_as_sprites.add(carteiro_andando)

# Grupo colisão com a carteira
grupo_obstaculo = pygame.sprite.Group()
grupo_colisao_poste=pygame.sprite.Group()

obstaculo = None

# São criados 2 fundos, um incial e outro logo após o primeiro, que aparece quando o primeiro sai da tela
bg_e = 0
bg_d = background.get_width()

# Iniciando a estrutura 
Start = True

# Rodando o cenário
clock = pygame.time.Clock()
velocidade_tela = 2.4

# Loop Principal!
while Start:
    clock.tick(config['fps'])
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

    # Velocidade com que o fundo se mexe
    bg_e -= velocidade_tela
    bg_d -= velocidade_tela

    # Quando os fundos saem completamente da tela, eles voltam para o início para passarem novamente
    if bg_e < background.get_width() * -1:
        bg_e = background.get_width()

    if bg_d < background.get_width() * -1:
        bg_d = background.get_width()

    if obstaculo == None or obstaculo.rect.x < 300:
        opcao = random.randint(1, 2)
        if opcao == 1:
            obstaculo = Cone(cone_img)
            grupo_obstaculo.add(obstaculo)
            
        if opcao == 2:
            obstaculo = Poste(poste_img)
            obstaculo_invisivel=Quadrado(poste_img)
            grupo_colisao_poste.add(obstaculo_invisivel)
        todas_as_sprites.add(obstaculo)
        todas_as_sprites.add(obstaculo_invisivel)
            

        

    colisoes = pygame.sprite.spritecollide(carteiro_andando, grupo_obstaculo, False, pygame.sprite.collide_mask)
    colisao_poste=pygame.sprite.spritecollide(carteiro_andando,grupo_colisao_poste,False,pygame.sprite.collide_mask)

    # Linhas importantes = Fazem o jogo ficar sempre se atualizando
    tela.blit(background, (bg_e, -270))
    tela.blit(background, (bg_d, -270))
    todas_as_sprites.draw(tela)

    # Caso colida com algum dos obstáculos, o fundo para de andar
    if colisoes or colisao_poste:
        velocidade_tela = 0
        pass
    else:
        todas_as_sprites.update()
        grupo_colisao_poste.update()

    pygame.display.update()

# Encerrando o PyGame
pygame.quit()
