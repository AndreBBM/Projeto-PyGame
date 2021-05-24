# Importando e iniciando pacotes
import pygame
from pygame.constants import QUIT

pygame.init()


# Criando a tela do jogo
# Dimensões
altura=500
largura=700
WIDTH_cart= "?"
WIDTH_bura= "?"
HEIGHT_cart= "?"
HEIGHT_bura= "?"

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Olha o Carteiro!')

# Carregando imagens: (Só estruturando)
background = pygame.image.load('').convert() # Não precisa de transparência aqui
carteiro_img = pygame.image.load('').convert_alpha()
carteiro_img= pygame.transform.scale(carteiro_img, (WIDTH_cart, HEIGHT_cart))
buracos_img = pygame.image.load('').convert_alpha()
buracos_img = pygame.transform.scale(buracos_img, (WIDTH_bura, HEIGHT_bura))

# Iniciando a estrutura 
Start = True

# Loop Principal!
while Start:
    tela.fill((176, 196, 222))
    # Tratando evento
    for event in pygame.event.get():
        # Para sair do jogo
        if event.type == QUIT:
            Start=False
    #Linha importante= Faz o jogo ficar sempre atualizando
    pygame.display.update()

pygame.quit()


