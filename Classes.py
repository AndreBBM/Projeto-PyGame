import pygame

# Criando classe da caixa
class Caixa(pygame.sprite.Sprite):
    def __init__(self, caixas_img):
        pygame.sprite.Sprite.__init__(self)
        self.image=caixas_img
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.center=(100,300)
    def update(self):
        if self.rect.topright[0]<0:
            self.rect.x=500
        self.rect.x-=2

class Poste (pygame.sprite.Sprite):
    def __init__(self,poste_img):
        pygame.sprite.Sprite.__init__(self)
        self.image=poste_img
        self.image=pygame.transform.scale(self.image,(100,200))
        self.rect=self.image.get_rect()
        #mascara de colisão
        self.mask=pygame.mask.from_surface(self.image)

        self.rect.center=(300,220)
    def update(self):
        if self.rect.topright[0]<0:
            self.rect.x=700
        self.rect.x-=5