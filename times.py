import pygame
from config import *
from assets import *

def tela_times(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    status = TIMES
    while status == TIMES:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT

            if event.type == pygame.MOUSEBUTTONDOWN:
                status = GAME
        window.fill((255, 255, 255))  # Preenche com a cor branca
        window.blit(assets[TIME_BACKGROUND], (0, 0))

        # ----- Atualiza estado do jogo
        pygame.display.update()
    return status
