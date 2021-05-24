# Importando e iniciando pacotes
import pygame
from pygame.constants import QUIT

pygame.init()

# Criando a tela do jogo
# Dimensões
altura = 400
largura = 700
WIDTH_cart= 100
WIDTH_bura= 100
HEIGHT_cart= 200
HEIGHT_bura= 200

buraco_x="?"
buraco_y="?"
carteiro_y=100
carteiro_x=140
buraco_speed="?"
carteiro_speedx="?"
carteiro_speedy="?"

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Olha o Carteiro!')

# Carregando imagens: (Só estruturando)
background = pygame.image.load('Imagens/8bitNY.jpg').convert() # Não precisa de transparência aqui
carteiro_img = pygame.image.load('Imagens/MailmanFemale.png').convert_alpha()
carteiro_img= pygame.transform.scale(carteiro_img, (WIDTH_cart, HEIGHT_cart))
buracos_img = pygame.image.load('Imagens/buraco.png').convert_alpha()
buracos_img = pygame.transform.scale(buracos_img, (WIDTH_bura, HEIGHT_bura))

# Iniciando a estrutura 
Start = True

# Loop Principal!
while Start:
    
    # Tratando evento
    for event in pygame.event.get():
        # Para sair do jogo
        if event.type == QUIT:
            Start = False
    
    # Velocidade do buraco no espaço    
    buraco_x += buraco_speed

    # Pra não sair da sala
    if buraco_x > "?": #Tamanho máximo da imagem
       buraco_x = " " #Tamanho inicial

    tela.fill((176, 196, 222))
    tela.blit(background, (0, 0))

    # Linha importante = Faz o jogo ficar sempre atualizando
    tela.blit(carteiro_img, (carteiro_x, carteiro_y))
    #Linha importante= Faz o jogo ficar sempre atualizando
    pygame.display.update()

pygame.quit()


