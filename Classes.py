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