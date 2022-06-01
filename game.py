import pygame
import random
from config import *
from assets import *
from sprites import *
from times import *

def tela_game(window, time, time_rival):
    clock = pygame.time.Clock()
    assets = load_assets()
    bola = Bola(assets[BOLA_IMAGE], 480, 620)
    goleiro = Goleiro(assets[GOLEIRO_IMAGE], 480, 452)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(goleiro)
    all_sprites.add(bola)
    status = GAME
    #ok = False
    while status == GAME:
        clock.tick(FPS)
        #rcolisao= pygame.sprite.spritecollide(bola,assets[GOLEIRO_IMAGE],False,pygame.sprite.collide_mask)
        #if colisao>0:
        #   window.blit(bola, 480, 620)
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                bola.shoot(pos_x, pos_y)
                goleiro.defense(pos_x, pos_y)
                ok = True
            #if ok:
                #status = AVISO_DEFESA

        all_sprites.update()

        # ----- Gera saidas
        window.fill((255, 255, 255))  # Preenche com a cor branca
        window.blit(assets[GAME_BACKGROUND], (0, 0))
        if time == 'brasil':
            window.blit(assets[BRASIL_IMAGE], (40, 40))
        elif time == 'franca':
            window.blit(assets[FRANCA_IMAGE], (40, 40)) 
        elif time == 'alemanha':
            window.blit(assets[ALEMANHA_IMAGE], (40, 40)) 
        elif time == 'argentina':
            window.blit(assets[ARGENTINA_IMAGE], (40, 40)) 

        if time_rival == 'brasil':
            window.blit(assets[BRASIL_IMAGE], (870, 40))
        elif time_rival == 'franca':
            window.blit(assets[FRANCA_IMAGE], (870, 40)) 
        elif time_rival == 'alemanha':
            window.blit(assets[ALEMANHA_IMAGE], (870, 40)) 
        elif time_rival == 'argentina':
            window.blit(assets[ARGENTINA_IMAGE], (870, 40)) 
        


        all_sprites.draw(window)
        cor = (255, 0, 0)

        
        # pygame.draw.polygon(window, cor, [(265,260),(685,260),(695,440),(250,440)])
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    return status
