# Importando e iniciando pacotes
import pygame
import os
from constantes import *
pygame.mixer.init()

# Para o efeito sonoro do pulo
diretorio_principal = os.path.dirname(__file__)
diretorio_sons = os.path.join(diretorio_principal, 'som')
som_do_pulo = pygame.mixer.Sound('Som/mb_jump.wav')

# Classe do carteiro
class Carteiro(pygame.sprite.Sprite):
    def __init__(self, carteiro_sheet):
        pygame.sprite.Sprite.__init__(self)
        # Colocando o som do pulo e aumentando o volume do som
        self.som_do_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'mb_jump.wav'))
        self.som_do_pulo.set_volume(0.9)
        # Faces da carteira e dimensionando escala
        self.img1 = carteiro_sheet.subsurface((0, 0), (235, 336))
        self.img1 = pygame.transform.scale(self.img1, (235 - 170, 336 - 250))
        self.img2 = carteiro_sheet.subsurface((0, 336), (235, 336))
        self.img2 = pygame.transform.scale(self.img2, (235 - 170, 336 - 250))
        self.img3 = carteiro_sheet.subsurface((235, 0), (235, 336))
        self.img3 = pygame.transform.scale(self.img3, (235 - 170, 336 - 250))
        self.imagens = [self.img1, self.img2, self.img3]
        self.index_lista = 0
        self.image = self.imagens[self.index_lista]
        self.rect = self.image.get_rect()
        # Criando máscara da sprite
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = carteiro_x
        self.rect.y = (chao-self.rect.height)
        self.inicial_y = carteiro_y - 250 // 4
        self.pular = False

    def pula(self):
        self.pular = True
        self.som_do_pulo.play()

    def update(self):
        if self.pular == True:
            if self.rect.y <= 150:
                self.pular = False
            self.rect.y -= 10
        if self.index_lista > 2:
            self.index_lista = 0
        else:
            if self.rect.y < self.inicial_y:
                self.rect.y += 5
            else:
                self.rect.y = self.inicial_y

        self.index_lista += 0.25
        self.image = self.imagens[int(self.index_lista)]

# Classe da caixa
class Caixa(pygame.sprite.Sprite):
    def __init__(self, caixas_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = caixas_img
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (largura, chao-self.rect.height)

    def update(self):
        if self.rect.x < -self.rect.width:
            self.kill()
        self.rect.x -= 2

# Classe do poste
class Poste(pygame.sprite.Sprite):
    def __init__(self, poste_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = poste_img
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.rect = self.image.get_rect()
        # Máscara de colisão
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = largura
        self.rect.y = (chao-self.rect.height)

    def update(self):
        if self.rect.x < -self.rect.width:
            self.kill()
        self.rect.x -= 2

# Classe do cone
class Cone(pygame.sprite.Sprite):
    def __init__(self, cone_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = cone_img
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        # Criando máscara da sprite
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = largura
        self.rect.y = (chao-self.rect.height)

    def update(self):
        if self.rect.x < -self.rect.width:
            self.kill()
        self.rect.x -= 2

class Lampada(pygame.sprite.Sprite):
    def __init__(self, poste_img,poste):
        pygame.sprite.Sprite.__init__(self)
        self.image = poste_img
        self.image = poste_img.subsurface((0, 0), (100, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (300,280)
        self.referencia_poste = poste
        self.rect.centerx = self.referencia_poste.rect.centerx

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.centerx = self.referencia_poste.rect.centerx
        self.rect.x -= 2
