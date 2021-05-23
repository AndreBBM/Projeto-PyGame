
import pygame
from pygame.constants import QUIT
pygame.init()

altura=500
largura=700

tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption('Olha o Carteiro!')

Start=True

#Loop Principal!
while Start:
    tela.fill((176, 196, 222))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #Linha importante= Faz o jogo ficar sempre atualizando
    pygame.display.update()


