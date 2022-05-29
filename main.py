import pygame
from aviso_chute import tela_aviso_chute
from aviso_defesa import tela_aviso_defesa
from config import *
from game import tela_game
from game_gk import tela_game_gk
from inicial import tela_inicial
from times import tela_times

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

time = ''
status = INICIAL
while status != QUIT:
    if status == INICIAL:
        status = tela_inicial(window)
    if status == TIMES:
        status, time, time_rival = tela_times(window)
    if status == GAME:
        status = tela_game(window, time, time_rival)
    if status == GAME_GK:
        status = tela_game_gk(window, time, time_rival) 
    if status == AVISO_CHUTE:
        status = tela_aviso_chute(window)
    if status == AVISO_DEFESA:
        status = tela_aviso_defesa(window)

pygame.quit()  

