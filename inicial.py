import pygame
from config import *
from assets import *
pygame.mixer.init()

pygame.mixer.music.load('hino_champions.mp3')
pygame.mixer.music.set_volume(0.4)

def tela_inicial(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    status = INICIAL
    while status == INICIAL:
        clock.tick(FPS)
        pygame.mixer.play()
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
    return status
