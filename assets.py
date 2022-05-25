import pygame
from config import *

INICIAL_BACKGROUND = 'inicial.background'
TIME_BACKGROUND = 'time.background'
BOLA_IMAGE = 'bola.image'
GAME_BACKGROUND = 'game.background'
GOLEIRO_IMAGE = 'goleiro.image'
CHUTEIRA_IMAGE = 'chuteira.image'
GOL_IMAGE = 'gol.image'

def load_assets():
    a = {}
    # ----- Inicia assets
    a[INICIAL_BACKGROUND] = pygame.image.load('Tela_inicial.png').convert()
    a[INICIAL_BACKGROUND] = pygame.transform.scale(a[INICIAL_BACKGROUND], (960, 720))
    a[BOLA_IMAGE] = pygame.image.load('Bola_de_futebol.png').convert_alpha()
    a[BOLA_IMAGE] = pygame.transform.scale(a[BOLA_IMAGE], (BOLA_WIDTH, BOLA_HEIGHT))
    a[GAME_BACKGROUND] = pygame.image.load('Imagem_jogo.jpg').convert_alpha()
    a[GAME_BACKGROUND] = pygame.transform.scale(a[GAME_BACKGROUND], (960, 720))
    a[GOLEIRO_IMAGE]= pygame.image.load('Goleiro.png').convert_alpha()
    a[GOLEIRO_IMAGE] = pygame.transform.scale(a[GOLEIRO_IMAGE], (GOLEIRO_WIDTH, GOLEIRO_HEIGHT))
    a[TIME_BACKGROUND] = pygame.image.load('Escolha_dos_times.jpg').convert_alpha()
    a[TIME_BACKGROUND] = pygame.transform.scale(a[TIME_BACKGROUND], (960, 720))
    a[CHUTEIRA_IMAGE] = pygame.image.load('soccer_boot.png').convert_alpha()
    a[CHUTEIRA_IMAGE] = pygame.transform.scale( a[CHUTEIRA_IMAGE], (CHUTEIRA_WIDTH, CHUTEIRA_HEIGHT))
    a[GOL_IMAGE] = pygame.image.load('gol.png').convert_alpha()
    a[GOL_IMAGE] = pygame.transform.scale(a[GOL_IMAGE], (680, 720))

    return a
