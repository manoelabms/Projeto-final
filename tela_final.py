import pygame
from config import *
from assets import *
#from main import *


def game_over(window, time_casa, time_rival, placar_casa, placar_visitante, rodadas):
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
                rodadas = 0


        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets[FIM_BACKGROUND], (0, 0))
        font = pygame.font.SysFont(None, 48)
        score = font.render('{0} {1} x {2} {3}'.format(time_casa, placar_casa, placar_visitante, time_rival), True, (255, 255, 255))
        score_rect = score.get_rect()
        score_rect.midtop = (WIDTH / 2,  410)
        window.blit(score, score_rect)


        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
    return status, time_casa, time_rival, placar_casa, placar_visitante, rodadas
