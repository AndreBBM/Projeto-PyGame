# Importando e iniciando pacotes
from typing import Set
import pygame
from pygame.constants import *
from random import *
from Classes import *
import Setup
config = Setup.LoadConfig()
pygame.init()

# Criando a tela do jogo
# Dimensões da tela
altura = 400
largura = 700
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Olha o Carteiro!')

# Dimensões das imagens colocadas
WIDTH_cart= 50
WIDTH_pole= 100
WIDTH_cone= 50
WIDTH_bura= 100
WIDTH_caixa= 50

HEIGHT_cart= 50
HEIGHT_pole= 200
HEIGHT_cone= 50
HEIGHT_bura= 50
HEIGHT_caixa= 50

# Posição inicial do carteiro
carteiro_y=300
carteiro_x=175

# Carregando imagens: somente estruturando
background = pygame.image.load('Imagens/8bitNY.jpg').convert() # Não precisa de transparência aqui
background = pygame.transform.scale(background, (1000, 800))
carteiro_sheet = pygame.image.load('Imagens/MailmanFemaleSpriteSheet.png').convert_alpha()
carteiro_img = pygame.image.load('Imagens/MailmanFemale.png').convert_alpha()
carteiro_img = pygame.transform.scale(carteiro_img, (WIDTH_cart, HEIGHT_cart))
poste_img = pygame.image.load('Imagens/poste.png').convert_alpha()
poste_img = pygame.transform.scale(poste_img, (WIDTH_pole, HEIGHT_pole))
buracos_img = pygame.image.load('Imagens/buraco.png').convert_alpha()
buracos_img = pygame.transform.scale(buracos_img, (WIDTH_bura, HEIGHT_bura))
caixas_img = pygame.image.load('Imagens/Caixa.jpg').convert_alpha()
caixas_img = pygame.transform.scale(caixas_img, (WIDTH_caixa, HEIGHT_caixa))
cone_img = pygame.image.load('Imagens/cone.png').convert_alpha()
cone_img = pygame.transform.scale(cone_img, (WIDTH_cone, HEIGHT_cone))

# Testando sprite - Carteiro
class Carteiro (pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        #Faces da carteira e dimensionando escala
        self.img1=carteiro_sheet.subsurface((0,0),(235,336))
        self.img1=pygame.transform.scale(self.img1, (235-170,336-250))
        self.img2=carteiro_sheet.subsurface((0,336),(235,336))
        self.img2=pygame.transform.scale(self.img2, (235-170, 336-250))
        self.img3=carteiro_sheet.subsurface((235,0),(235,336))
        self.img3=pygame.transform.scale(self.img3, (235-170, 336-250))
        self.imagens=[self.img1,self.img2,self.img3]
        self.index_lista=0
        self.image=self.imagens[self.index_lista]
        self.rect=self.image.get_rect()
        #Criando máscara da sprite
        self.mask=pygame.mask.from_surface(self.image)
        
        self.rect.center = (170, 300)
        self.inicial_y= carteiro_y - 250//4
        self.pular=False

    def pula(self):
        self.pular = True

    def update(self):
        if self.pular == True:
            if self.rect.y <= 50:
                self.pular = False
            self.rect.y -= 10
        if self.index_lista>2:
            self.index_lista=0
        else:
            if self.rect.y < self.inicial_y:
                self.rect.y +=5
            else:
                self.rect.y= self.inicial_y
            
        self.index_lista+=0.25
        self.image=self.imagens[int(self.index_lista)]

# Classe do poste = Obstáculo de cima 
class Poste (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=poste_img
        self.image=pygame.transform.scale(self.image,(100,200))
        self.rect=self.image.get_rect()
        self.rect.center=(300,220)
    def update(self):
        if self.rect.topright[0]<0:
            self.rect.x=700
        self.rect.x-=2

# Criando classe do cone
class Cone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=cone_img
        self.image=pygame.transform.scale(self.image,(60,60))
        self.rect=self.image.get_rect()
        #Criando mascara da sprite
        self.mask=pygame.mask.from_surface(self.image)

        self.rect.center=(300,290)
    def update(self):
        if self.rect.topright[0]<0:
            self.rect.x=800
        self.rect.x-= 2

todas_as_sprites = pygame.sprite.Group()
colisoes_com_carteiro= pygame.sprite.Group()
cone = Cone()
colisoes_com_carteiro.add(cone)
poste = Poste()
carteiro_andando = Carteiro()
caixa = Caixa(caixas_img)
todas_as_sprites.add(poste)
todas_as_sprites.add(cone)
todas_as_sprites.add(caixa)
todas_as_sprites.add(carteiro_andando)

#Grupo colisão cone-carteira
grupo_obstaculos=pygame.sprite.Group()
grupo_obstaculos.add(cone)



# São criados 2 fundos, um incial e outro logo após o primeiro, que aparece quando o primeiro sai da tela
bg_e = 0
bg_d = background.get_width()

# Iniciando a estrutura 
Start = True

# Rodando o cenário
clock = pygame.time.Clock()
FramesPerSecond=24
velocidade_tela=2.4
# Loop Principal!
while Start:
    config = Setup.LoadConfig()
    altura = config['altura']
    largura = config['largura']
    FramesPerSecond = config['fps']
    tela = pygame.display.set_mode((largura,altura))
    clock.tick(FramesPerSecond)
    # Tratando eventos
    for event in pygame.event.get():
        # Para sair do jogo
        if event.type == QUIT:
            Start = False
        # Para pular
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if carteiro_andando.rect.y!= carteiro_andando.inicial_y:
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

    # Para o carteiro não sair da sala
    if carteiro_x > 700: # Tamanho máximo da imagem
       carteiro_x = 0    # Tamanho inicial

    colisoes=pygame.sprite.spritecollide(carteiro_andando,grupo_obstaculos,False,pygame.sprite.collide_mask)
    
    tela.fill((176, 196, 222))
    # Linhas importantes = Fazem o jogo ficar sempre se atualizando
    tela.blit(background, (bg_e, -370))
    tela.blit(background, (bg_d, -370))
    todas_as_sprites.draw(tela)

    if colisoes:
        velocidade_tela=0
        pass
    else:
        todas_as_sprites.update()
        
    pygame.display.update()

# Encerrando o PyGame
pygame.quit()


