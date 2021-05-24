import pygame

WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')

carteiro = pygame.image.load('Imagens/MailmanFemale.png').convert()
carteira = pygame.image.load('Imagens/MailmanMale.png').convert()
cidade = pygame.image.load('Imagens/8bitNY.jpg').convert()
buraco = pygame.image.load('Imagens/buraco.png').convert()


