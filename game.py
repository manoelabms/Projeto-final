import pygame
from config import *
from assets import *
from sprites import *

def tela_game(window, time):
    clock = pygame.time.Clock()
    assets = load_assets()
    bola = Bola(assets[BOLA_IMAGE], 480, 620)
    goleiro = Goleiro(assets[GOLEIRO_IMAGE], 480, 452)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(goleiro)
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
                goleiro.shoot(pos_x, pos_y)

        all_sprites.update()

        # ----- Gera saidas
        window.fill((255, 255, 255))  # Preenche com a cor branca
        window.blit(assets[GAME_BACKGROUND], (0, 0))
        if time == 'brasil':
            window.blit(assets[BRASIL_IMAGE], (50, 50)) 
        elif time == 'franca':
            window.blit(assets[FRANCA_IMAGE], (50, 50)) 
        elif time == 'alemanha':
            window.blit(assets[ALEMANHA_IMAGE], (50, 50)) 
        elif time == 'argentina':
            window.blit(assets[ARGENTINA_IMAGE], (50, 50)) 
        all_sprites.draw(window)
        cor = (255, 0, 0)
        # pygame.draw.polygon(window, cor, [(265,260),(685,260),(695,440),(250,440)])
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    return status
