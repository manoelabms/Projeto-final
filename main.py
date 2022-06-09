import pygame
from aviso_chute import tela_aviso_chute
from aviso_defesa import tela_aviso_defesa
from config import *
from game import tela_game
from game_gk import tela_game_gk
from inicial import tela_inicial
from tela_final import game_over
from times import tela_times

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

time_casa = ''
time_rival = ''
rodadas = 1
placar_casa = 0
placar_visitante = 0

pygame.mixer.init()
pygame.mixer.music.set_volume(0.8)



status = INICIAL
while status != QUIT:
    if status == INICIAL:
        status, placar_casa, placar_visitante = tela_inicial(window, placar_casa, placar_visitante)
    if status == TIMES:
        status, time_casa, time_rival = tela_times(window)
    if status == GAME:
        status, rodadas, placar_casa, placar_visitante = tela_game(window, time_casa, time_rival, rodadas, placar_casa, placar_visitante)
    if status == GAME_GK:
        status, rodadas, placar_casa, placar_visitante = tela_game_gk(window, time_casa, time_rival, rodadas, placar_casa, placar_visitante) 
    if status == AVISO_CHUTE:
        status = tela_aviso_chute(window)
    if status == AVISO_DEFESA:
        status = tela_aviso_defesa(window)
    if status == GAME_OVER:
        status, time_casa, time_rival, placar_casa, placar_visitante, rodadas = game_over(window, time_casa, time_rival, placar_casa, placar_visitante, rodadas)


pygame.quit()  

