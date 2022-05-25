import pygame
from config import *
from assets import *
from sprites import *

def tela_game(window):
    clock = pygame.time.Clock()
    assets = load_assets()

    bola = None
    goleiro = None
    chuteira = None
    all_sprites = pygame.sprite.Group()
    gol = None
    status = GAME
    while status == GAME:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT

        if bola == None:
            bola = Bola(assets[BOLA_IMAGE], 480, 720)
            all_sprites.add(bola)

        if goleiro == None:
            goleiro = Goleiro(assets[GOLEIRO_IMAGE], 480, 560)
            all_sprites.add(goleiro)

        if chuteira == None:
            chuteira = Chuteira(assets[CHUTEIRA_IMAGE], 400, 560)
            all_sprites.add(chuteira)
        
        if gol == None:
            gol = Gol(assets[GOL_IMAGE,480,360])
        all_sprites.update()

        # ----- Gera saidas
        window.fill((255, 255, 255))  # Preenche com a cor branca
        window.blit(assets[GAME_BACKGROUND], (0, 0))

        all_sprites.draw(window)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    return status
