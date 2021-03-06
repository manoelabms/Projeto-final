import pygame
from config import *
import random

class Bola(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = img
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.profundidade = 1
        self.chutou = False
        self.d_x = 0
        self.d_y = 0
        self.tx = 0
        self.ty = 0
        self.d_b = 0
        self.px = self.rect.centerx
        self.py = self.rect.centery
        self.w = self.image.get_rect().width
        self.h = self.image.get_rect().height
      
    def update(self):
        if self.chutou and self.profundidade > 0:
            self.px += self.d_x
            self.py += self.d_y
            self.rect.centerx = self.px
            self.rect.centery = self.py
            center = self.rect.center
            self.w -= self.d_b
            self.h -= self.d_b
            self.image = pygame.transform.scale(self.image_original, (self.w, self.h))
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.profundidade -= 1
        
    def shoot(self, tx, ty, p = PROFUNDIDADE):
        print(tx, ty)
        if not self.chutou:
            self.profundidade = p
            self.tx = tx
            self.ty = ty
            self.d_x = (tx - self.rect.centerx) / self.profundidade
            self.d_y = (ty - self.rect.centery) / self.profundidade
            self.d_b = (self.rect.width - 50) / self.profundidade
            self.w = self.image.get_rect().width
            self.h = self.image.get_rect().height
            self.px = self.rect.centerx
            self.py = self.rect.centery
            self.chutou = True

class Bola_gk(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = img
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.profundidade = 1
        self.chutou = False
        self.d_x = 0
        self.d_y = 0
        self.tx = 0
        self.ty = 0
        self.d_b = 0
        self.px = self.rect.centerx
        self.py = self.rect.centery

        self.w = self.image.get_rect().width
        self.h = self.image.get_rect().height

    def update(self):
        if self.chutou and self.profundidade > 0:
            self.px += self.d_x
            self.py += self.d_y
            self.rect.centerx = self.px
            self.rect.centery = self.py
            center = self.rect.center
            self.w -= self.d_b
            self.h -= self.d_b
            self.image = pygame.transform.scale(self.image_original, (self.w, self.h))
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.profundidade -= 1
        
    def shoot(self, tx, ty, p = PROFUNDIDADE):
        if not self.chutou:
            self.profundidade = p
            self.tx = tx
            self.ty = ty
            aleatorio = random.randint(1, 5)
            if aleatorio != 2:
                tx = random.randint(250, 695)
                ty = random.randint(260, 440)
            self.d_x = (tx - self.rect.centerx) / self.profundidade
            self.d_y = (ty - self.rect.centery) / self.profundidade
            self.d_b = (self.rect.width - 50) / self.profundidade
            self.w = self.image.get_rect().width
            self.h = self.image.get_rect().height
            self.px = self.rect.centerx
            self.py = self.rect.centery
            self.chutou = True

class Goleiro(pygame.sprite.Sprite):
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
        self.speedx = 0
        self.profundidade = 300
        self.defesa = False
        self.ty = 0
        self.tx = 0

    def update(self):
        if self.defesa and self.ty < self.rect.bottom:
            if self.profundidade > 0:
                self.rect.width -= 2
                self.rect.height -= 2
                self.rect.centerx += self.d_x
                self.rect.centery += self.d_y
                self.profundidade -= 1
            else:
                self.profundidade = 0

    def defense(self, tx, ty):
        if not self.defesa:
            aleatorio = random.randint(1, 5)
            if aleatorio != 2:
                tx = random.randint(250, 695)
                ty = random.randint(260, 440) 
            self.d_x = (tx - self.ini_x) // 100
            self.d_y = (ty - self.ini_y) // 100
            self.ty = ty
            self.tx = tx
            self.defesa = True



class Goleiro_gk(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = img
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.profundidade = 1
        self.defesa = False
        self.d_x = 0
        self.d_y = 0
        self.tx = 0
        self.ty = 0
        self.d_b = 0
        self.w = self.image.get_rect().width
        self.h = self.image.get_rect().height
        self.px = self.rect.centerx
        self.py = self.rect.centery
      
    def update(self):
        if self.defesa and self.profundidade > 0:
            self.px += self.d_x
            self.py += self.d_y
            self.rect.centerx = self.px
            self.rect.centery = self.py
            self.profundidade -= 1

    def defense (self, tx, ty, p = PROFUNDIDADE):
        if not self.defesa:
            self.profundidade = p
            self.tx = tx
            self.ty = ty
            self.d_x = (tx - self.rect.centerx) / self.profundidade
            self.d_y = (ty - self.rect.centery) / self.profundidade
            self.d_b = (self.rect.width - 50) / self.profundidade
            self.px = self.rect.centerx
            self.py = self.rect.centery
            self.defesa = True
