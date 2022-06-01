import pygame
from config import *
import random


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
        self.image_original = img
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.ini_x = x
        self.ini_y = y
        self.d_x = 0
        self.d_y = 0
        self.speedx = 1
        self.profundidade = 150
        self.chutou = False
        self.tx = 0
        self.ty = 0
        self.d_b = (self.rect.width - 50) / 100
      

    def update(self):
        parada = False
        if self.chutou and self.ty < self.rect.centery:
            if self.profundidade > 0:

                self.rect.centerx += int(self.d_x)
                self.rect.centery += int(self.d_y)
                w = self.image.get_rect().width * .99
                if w > 50:
                    center = self.rect.center
                    # TODO: rescalar a imagem
                    print(self.image.get_width(), self.image.get_height())
                    w = self.image.get_rect().width - self.d_b
                    h = self.image.get_rect().height - self.d_b
                    self.image = pygame.transform.scale(self.image_original,(w, h))
                    #self.image = self.explosion_anim[self.frame]

                    self.rect = self.image.get_rect()
                    self.rect.center = center
                self.profundidade -= 1
                
                #if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
                    #self.rect.centerx = 480
                    #self.rect.bottom = 0
            else:
                self.profundidade = 0
        elif self.rect.centery < self.ty: 
            parada = True
        return parada
        
    def shoot(self, tx, ty):
        print(tx, ty)
        if not self.chutou:
            self.tx = tx
            self.ty = ty
            self.d_x = (tx - self.rect.centerx) / 100
            self.d_y = (ty - self.rect.centery) / 100
            self.chutou = True

class Bola_gk(pygame.sprite.Sprite):
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
                if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
                    self.rect.centerx = 480
                    self.rect.bottom = 0
            else:
                self.profundidade = 0
        
    def shoot(self, tx, ty):
        print(tx, ty)
        if not self.chutou:
            self.d_x = random.randint(0,960)
            self.d_y = random.randint(0,720) 
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
        self.hitbox = (self.rect.centerx, self.rect.bottom, 140, 160)
        

# The elements in the hitbox are (top left x, top left y, width, height)
        #pygame.draw.polygon(window, cor, [(265,260),(685,260),(695,440),(250,440)])

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
            if random.randint(2, 3) == 3:
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
        self.chutou = False
        

    def update(self):
        if self.chutou:
            if self.profundidade > 0:
                self.rect.width -= 2
                self.rect.height -= 2
                self.rect.centerx += self.d_x
                self.rect.centery += self.d_y
                self.profundidade -= 1
            else:
                self.profundidade = 0

    def defense (self, tx, ty):
        print(tx, ty)
        if not self.defense:
            self.d_x = (tx - self.ini_x) // 100
            self.d_y = (ty - self.ini_y) // 100
            self.chutou = True

