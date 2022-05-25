import pygame
from config import *
from assets import *
from sprites import *

def tela_game(window, time):
    clock = pygame.time.Clock()
    assets = load_assets()

    bola = Bola(assets[BOLA_IMAGE], 480, 720)
    goleiro = Goleiro(assets[GOLEIRO_IMAGE], 480, 560)
    chuteira = Chuteira(assets[CHUTEIRA_IMAGE], 400, 560)
    gol = Gol(assets[GOL_IMAGE], 480, 800)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(gol)
    all_sprites.add(goleiro)
    all_sprites.add(chuteira)
    all_sprites.add(bola)
    status = GAME
    while status == GAME:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                bola.shoot(pos_x, pos_y)

        all_sprites.update()

        # ----- Gera saidas
        window.fill((255, 255, 255))  # Preenche com a cor branca
        window.blit(assets[GAME_BACKGROUND], (0, 0))

        all_sprites.draw(window)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    return status
