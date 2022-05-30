import pygame
from config import *
from assets import *

def tela_aviso_chute(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    status = AVISO_CHUTE
    while status == AVISO_CHUTE:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT
            # ----- Verifica consequências
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = GAME

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets[TELA_AVISO_CHUTE], (0, 0))

        

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
    return status
