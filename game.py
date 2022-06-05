import pygame
import random
from config import *
from assets import *
from sprites import *
from times import *
import time

def tela_game(window, time_casa, time_rival):
    clock = pygame.time.Clock()
    assets = load_assets()
    bola = Bola(assets[BOLA_IMAGE], 480, 620)
    goleiro = Goleiro(assets[GOLEIRO_IMAGE], 480, 452)
    all_goleiros = pygame.sprite.Group()
    all_goleiros.add(goleiro)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(goleiro)
    all_sprites.add(bola)
    status = GAME

    while status == GAME:
        clock.tick(FPS)
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.time.set_timer(pygame.USEREVENT+1, 10000)
                pos_x, pos_y = pygame.mouse.get_pos()
                bola.shoot(pos_x, pos_y)
                goleiro.defense(pos_x, pos_y)
            if event.type == pygame.USEREVENT+1: 
                pygame.time.set_timer(pygame.USEREVENT+1, 0) 
                status = AVISO_DEFESA
        all_sprites.update()
        
        hits = pygame.sprite.spritecollide(bola, all_goleiros, False, pygame.sprite.collide_mask)
        if bola.profundidade == 0 and len(hits) > 0:
            print('pegou')
            placar_fora += 1

        elif bola.profundidade == 0:
            if pos_x > 265 and pos_x < 685 and pos_y > 260 and pos_y < 440:
                print('gol')
            #[(265,260),(685,260),(695,440),(250,440)])
        else:
            print('n gol')
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
