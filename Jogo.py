
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
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #Linha importante= Faz o jogo ficar sempre atualizando
    pygame.display.update()


