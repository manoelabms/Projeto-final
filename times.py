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
                    if pos_x > 540 and pos_x < 878 and pos_y > 457 and pos_y < 557:
                        time_casa = 'Alemanha'
                    elif pos_x > 80 and pos_x < 418 and pos_y > 457 and pos_y < 557:
                        time_casa = 'Argentina'
                    elif pos_x > 80 and pos_x < 353 and pos_y > 230 and pos_y < 330:
                        time_casa = 'Brasil'
                    elif pos_x > 540 and pos_x < 815 and pos_y > 235 and pos_y < 340:
                        time_casa = 'França'

                    time_rival = random.choice(lista_times)
                    while time_rival == time_casa:
                        time_rival = random.choice(lista_times)
                        
                    status = AVISO_CHUTE
        window.fill((255, 255, 255)) 
        window.blit(assets[TIME_BACKGROUND], (0, 0))
    
        cor = (255, 0, 0)
        vertices_alemanha = (540, 457, 338, 100)
        pygame.draw.rect(window, cor, vertices_alemanha)
        vertices_argentina = (80, 457, 338, 100)
        pygame.draw.rect(window, cor, vertices_argentina)
        vertices_brasil = (80, 230, 273, 100)
        pygame.draw.rect(window, cor, vertices_brasil)
        vertices_franca = (540, 235, 275, 105)
        pygame.draw.rect(window, cor, vertices_franca)

        # ----- Atualiza estado do jogo
        pygame.display.update()
    return status, time_casa, time_rival

