# Importando e iniciando pacotes
from typing import Set
import pygame
from pygame.constants import QUIT
import Setup
config = Setup.LoadConfig()
pygame.init()

# Criando a tela do jogo
# Dimensões
altura = 400
largura = 700
WIDTH_cart= 50
WIDTH_bura= 100
HEIGHT_cart= 50
HEIGHT_bura= 200

buraco_x="?"
buraco_y="?"
carteiro_y=300
carteiro_x=0
buraco_speed="?"
carteiro_speedx=1
carteiro_speedy="?"

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Olha o Carteiro!')

# Carregando imagens: (Só estruturando)
background = pygame.image.load('Imagens/8bitNY.jpg').convert() # Não precisa de transparência aqui
background= pygame.transform.scale(background, (1000, 800))
carteiro_img = pygame.image.load('Imagens/MailmanFemale.png').convert_alpha()
carteiro_img= pygame.transform.scale(carteiro_img, (WIDTH_cart, HEIGHT_cart))
buracos_img = pygame.image.load('Imagens/buraco.png').convert_alpha()
buracos_img = pygame.transform.scale(buracos_img, (WIDTH_bura, HEIGHT_bura))

#são criados 2 fundos, um incial e outro logo após o primeiro, que aparece quando o primeiro sai da tela
bg_e = 0
bg_d = background.get_width()

# Iniciando a estrutura 
Start = True

clock = pygame.time.Clock()
FramesPerSecond=24
# Loop Principal!
while Start:
    config = Setup.LoadConfig()
    altura = config['altura']
    largura = config['largura']
    FramesPerSecond = config['fps']
    tela = pygame.display.set_mode((largura,altura))
    clock.tick(FramesPerSecond)
    # Tratando evento
    for event in pygame.event.get():
        # Para sair do jogo
        if event.type == QUIT:
            Start = False

    #velocidade com que o fundo se mexe
    bg_e -= 2.4
    bg_d -= 2.4

    #quando os fundos saem completamente da tela eles voltam para o início para passarem de novo 
    if bg_e < background.get_width() * -1:
        bg_e = background.get_width()
    if bg_d < background.get_width() * -1:
        bg_d = background.get_width()
    # Velocidade do buraco no espaço    

    # Pra não sair da sala
    if carteiro_x > 700: #Tamanho máximo da imagem
       carteiro_x = 0 #Tamanho inicial

    tela.fill((176, 196, 222))

    # Linha importante = Faz o jogo ficar sempre atualizando
    tela.blit(carteiro_img, (carteiro_x, carteiro_y))
    #Linha importante= Faz o jogo ficar sempre atualizando, junto com o fundo

    tela.blit(background, (bg_e, -370))
    tela.blit(background, (bg_d, -370))
    tela.blit(carteiro_img, (carteiro_x, carteiro_y))

    pygame.display.update()

pygame.quit()


