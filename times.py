import pygame
from config import *
from assets import *

def tela_times(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    status = TIMES
    time = 'brasil'
    while status == TIMES:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                #if pos_x < 200 and po
                time = 'alemanha'
                status = GAME
        window.fill((255, 255, 255))  # Preenche com a cor branca
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
    return status, time
