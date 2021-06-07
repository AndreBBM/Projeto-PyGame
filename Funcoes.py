import pygame
from pygame.constants import *
from constantes import *

# Exibir mensagens:
def mensagem(msg, tamanho, cor):
    fonte = pygame.font.Font('Assets/font/PressStart2P.ttf', tamanho)
    mensagem = f"{msg}"  # F--F string--- Mesma coisa que .format
    texto_formatado = fonte.render(mensagem, True, cor)  # Textocerrilhado- Segundo
    return texto_formatado
