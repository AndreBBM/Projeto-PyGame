# Importando e iniciando pacotes
#from typing import Set
from pygame.constants import *
from Classes import *
from constantes import *
import pygame
tela = pygame.display.set_mode((largura, altura))

import LoopJogo
import LoopTelaInicial


state = INICIANDO
while state != DESISTINDO:
    if state == INICIANDO:
        state = LoopTelaInicial.executar(tela)
    elif state == JOGANDO:
        state = LoopJogo.executar(tela)
    else:
        state = DESISTINDO

# Encerrando o PyGame
pygame.quit()
