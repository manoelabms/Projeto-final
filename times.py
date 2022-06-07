import pygame
import random
from config import *
from assets import *

def tela_times(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    status = TIMES
    time_casa = '' #inicializando um time
    time_rival = '' #inicializando um time rival

    while status == TIMES:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT

            if event.type == pygame.MOUSEBUTTONDOWN:        
                    pos_x, pos_y = pygame.mouse.get_pos()
                    if pos_x > 540 and pos_x < 790 and pos_y > 410 and pos_y < 670:
                        time_casa = 'Real Madrid'
                    elif pos_x > 190 and pos_x < 440 and pos_y > 410 and pos_y < 670:
                        time_casa = 'Manchester United'
                    elif pos_x > 190 and pos_x < 410 and pos_y > 160 and pos_y < 390:
                        time_casa = 'Bayern Munchen'
                    elif pos_x > 540 and pos_x < 760 and pos_y > 120 and pos_y < 370:
                        time_casa = 'Paris Saint-Germain'

                    time_rival = random.choice(lista_times)
                    while time_rival == time_casa:
                        time_rival = random.choice(lista_times)
                        
                    status = AVISO_CHUTE
        window.fill((255, 255, 255)) 
        window.blit(assets[TIME_BACKGROUND], (0, 0))
    
        cor = (255, 0, 0)
        #vertices_madrid = (540, 410, 250, 260)
        #pygame.draw.rect(window, cor, vertices_madrid)
        #vertices_united = (190, 410, 250, 260)
        #pygame.draw.rect(window, cor, vertices_united)
        #vertices_bayern = (190, 160, 220, 230)
        #pygame.draw.rect(window, cor, vertices_bayern)
        #vertices_psg = (540, 120, 220, 250)
        #pygame.draw.rect(window, cor, vertices_psg)

        # ----- Atualiza estado do jogo
        pygame.display.update()
    return status, time_casa, time_rival

