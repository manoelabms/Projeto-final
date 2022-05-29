import pygame
from config import *
from game import tela_game
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
    
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

