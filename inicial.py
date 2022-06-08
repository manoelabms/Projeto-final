import pygame
from config import *
from assets import *

def tela_inicial(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    status = INICIAL
    pygame.mixer.music.load('hino_champions.mp3')
    pygame.mixer.music.play()
    while status == INICIAL:
        clock.tick(FPS)
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT
            # ----- Verifica consequências
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = TIMES

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets[INICIAL_BACKGROUND], (0, 0))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
    pygame.mixer.music.pause()
    return status
