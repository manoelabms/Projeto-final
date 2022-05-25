import pygame
from config import *

class Chuteira(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 1.5
    

class Bola(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.ini_x = x
        self.ini_y = y
        self.d_x = 0
        self.d_y = 0
        self.speedx = 1
        self.profundidade = 300
        self.chutou = False

    def update(self):
        if self.chutou:
            if self.profundidade > 0:
                self.rect.width -= 2
                self.rect.height -= 2
                self.rect.centerx += self.d_x
                self.rect.centery += self.d_y
                self.profundidade -= 2
            else:
                self.profundidade = 0

    def shoot(self, tx, ty):
        print(tx, ty)
        if not self.chutou:
            self.d_x = (tx - self.ini_x) // 100
            self.d_y = (ty - self.ini_y) // 100
            self.chutou = True

class Goleiro(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0

class Gol(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0