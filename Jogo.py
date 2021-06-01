# Importando e iniciando pacotes
#from typing import Set
from pygame.constants import *
from Classes import *
from constantes import *
import pygame
tela = pygame.display.set_mode((largura, altura))

import LoopJogo
import LoopTelaInicial


state = ACABOU
while state != MORTO:
    if state == ACABOU:
        state = LoopTelaInicial.executartelainicial(tela)
    elif state == JOGAR:
        state = LoopJogo.executarjoguinho(tela)
    else:
        state = MORTO

# Encerrando o PyGame
pygame.quit()
