import pygame
import random
from config import *
from assets import *
from sprites import *
from times import *

def tela_game_gk(window, time_casa, time_rival):
    clock = pygame.time.Clock()
    assets = load_assets()
    bola = Bola_gk(assets[BOLA_IMAGE], 480, 620)
    goleiro = Goleiro_gk(assets[GOLEIRO_IMAGE], 480, 370)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(goleiro)
    all_sprites.add(bola)
    status = GAME_GK
    while status == GAME_GK:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                bola.shoot(pos_x, pos_y)
                goleiro.defense(pos_x, pos_y)

        all_sprites.update()

        # ----- Gera saidas
        window.fill((255, 255, 255))  # Preenche com a cor branca
        window.blit(assets[GAME_BACKGROUND], (0, 0))
        if time_casa == 'brasil':
            window.blit(assets[BRASIL_IMAGE], (40, 40))
        elif time_casa == 'franca':
            window.blit(assets[FRANCA_IMAGE], (40, 40)) 
        elif time_casa == 'alemanha':
            window.blit(assets[ALEMANHA_IMAGE], (40, 40)) 
        elif time_casa == 'argentina':
            window.blit(assets[ARGENTINA_IMAGE], (40, 40)) 

        if time_rival == 'brasil':
            window.blit(assets[BRASIL_IMAGE], (900, 40))
        elif time_rival == 'franca':
            window.blit(assets[FRANCA_IMAGE], (900, 40)) 
        elif time_rival == 'alemanha':
            window.blit(assets[ALEMANHA_IMAGE], (900, 40)) 
        elif time_rival == 'argentina':
            window.blit(assets[ARGENTINA_IMAGE], (900, 40)) 

        all_sprites.draw(window)
        cor = (255, 0, 0)
        # pygame.draw.polygon(window, cor, [(265,260),(685,260),(695,440),(250,440)])
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    return status
