# Importando e iniciando pacotes
# from typing import Set
from pygame.constants import *
from Classes_Funcoes import *
from constantes import *
import pygame

tela = pygame.display.set_mode((largura, altura))

# Importando as três telas do jogo
import LoopJogo
import LoopTelaInicial
import LoopTelaInfo

state = ACABOU
# Enquanto diferente de morto
while state != MORTO:
    # Se acabou, aparece a tela inicial
    if state == ACABOU:
        state = LoopTelaInicial.executar_tela_inicial(tela)
    # Apertou espaço na tela inicial:
    elif state == INFO:
        state = LoopTelaInfo.executar_tela_info(tela)
    # Se jogar, mostrar a tela do jogo em si
    elif state == JOGAR:
        state = LoopJogo.executar_joguinho(tela)
    # Em todos os outros casos, ele está morto
    else:
        state = MORTO

# Encerrando o PyGame
pygame.quit()
