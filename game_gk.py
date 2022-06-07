import pygame
import random
from config import *
from assets import *
from sprites import *
from times import *

def tela_game_gk(window, time_casa, time_rival, rodadas, placar_casa, placar_visitante):
    clock = pygame.time.Clock()
    assets = load_assets()
    bola = Bola_gk(assets[BOLA_IMAGE], 480, 620)
    goleiro = Goleiro_gk(assets[GOLEIRO_IMAGE], 480, 370)
    all_goleiros = pygame.sprite.Group()
    all_goleiros.add(goleiro)
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
                pygame.time.set_timer(pygame.USEREVENT+1, 7000)
                pos_x, pos_y = pygame.mouse.get_pos()
                bola.shoot(pos_x, pos_y)
                goleiro.defense(pos_x, pos_y)
                rodadas +=1 
            if event.type == pygame.USEREVENT+1: 
                pygame.time.set_timer(pygame.USEREVENT+1, 0)
                if rodadas < 6: 
                    status = AVISO_CHUTE
                else:
                    status = GAME_OVER
                
        all_sprites.update()
        hits = pygame.sprite.spritecollide(bola, all_goleiros, False, pygame.sprite.collide_mask)
        if bola.profundidade == 0 and len(hits) > 0:
            print('pegou')


        elif bola.profundidade == 0:
            if pos_x > 265 and pos_x < 685 and pos_y > 260 and pos_y < 440:
                print('gol')
                placar_visitante += 1
               
        else:
            print('n gol')
        # ----- Gera saidas
        window.fill((255, 255, 255))  # Preenche com a cor branca
        window.blit(assets[GAME_BACKGROUND], (0, 0))
        if time_casa == 'PSG':
            window.blit(assets[PSG_IMAGE], (80, 20))
        elif time_casa == 'MAN':
            window.blit(assets[MANCHESTER_IMAGE], (80, 20)) 
        elif time_casa == 'RMA':
            window.blit(assets[REALMADRID_IMAGE], (80, 20)) 
        elif time_casa == 'FCB':
            window.blit(assets[BAYERN_IMAGE], (80, 20)) 

        if time_rival == 'PSG':
            window.blit(assets[PSG_IMAGE], (830, 20))
        elif time_rival == 'MAN':
            window.blit(assets[MANCHESTER_IMAGE], (830, 20)) 
        elif time_rival == 'RMA':
            window.blit(assets[REALMADRID_IMAGE], (830, 20)) 
        elif time_rival == 'FCB':
            window.blit(assets[BAYERN_IMAGE], (830, 20)) 

        all_sprites.draw(window)
        cor = (255, 0, 0)
        font = pygame.font.SysFont(None, 48)
        score = font.render('{0} {1} x {2} {3}'.format(time_casa, placar_casa, placar_visitante, time_rival), True, (255, 255, 255))
        score_rect = score.get_rect()
        score_rect.midtop = (WIDTH / 2,  50)
        window.blit(score, score_rect)
        round = font.render('Rodada {0}'.format(rodadas), True, (255, 255, 255))
        round_rect = round.get_rect()
        round_rect.midtop = (WIDTH / 2,  10)
        window.blit(round, round_rect)

    
        pygame.display.update()  # Mostra o novo frame para o jogador

    return status, rodadas, placar_casa, placar_visitante
