import pygame
from config import *
from assets import *
#from main import *

def game_over(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    status = GAME_OVER
    while status == GAME_OVER:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT
            # ----- Verifica consequências
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = INICIAL

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets[FIM_BACKGROUND], (0, 0))

        

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
    return status
