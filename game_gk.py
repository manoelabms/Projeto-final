import pygame
import random
from config import *
from assets import *
from sprites import *
from times import *

def tela_game_gk(window, time_casa, time_rival, rodadas, placar_casa, placar_visitante):
    pygame.mixer.music.load('som_torcida (2).mp3')
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    assets = load_assets()
    bola = Bola_gk(assets[BOLA_IMAGE], 480, 620)
    goleiro = Goleiro_gk(assets[GOLEIRO_IMAGE], 480, 370)
    all_goleiros = pygame.sprite.Group()
    all_goleiros.add(goleiro)
    all_sprites = pygame.sprite.Group()
    all_bolas = pygame.sprite.Group()
    all_bolas.add(bola)
    all_sprites.add(goleiro)
    all_sprites.add(bola)
    status = GAME_GK
    defendeu = False
    pygame.mixer.Sound.play(assets['apito'])
    while status == GAME_GK:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT
            if event.type == pygame.MOUSEBUTTONDOWN and not defendeu:
                pygame.time.set_timer(pygame.USEREVENT+1, 5000)
                pos_x, pos_y = pygame.mouse.get_pos()
                bola.shoot(pos_x, pos_y)
                goleiro.defense(pos_x, pos_y)
                defendeu = True
                #rodadas +=1 
            if event.type == pygame.USEREVENT+1: 
                pygame.time.set_timer(pygame.USEREVENT+1, 0)
                defendeu = False
                rodadas +=1
                if rodadas <= 5: 
                    status = AVISO_CHUTE
                else:
                    status = GAME_OVER
                
        all_sprites.update()
        hits = pygame.sprite.groupcollide(all_bolas, all_goleiros, False, False, None)
        if bola.profundidade == 0 and len(hits) > 0:
            for bola in hits:
                bola.kill()
                goleiro.kill()
                goleiro = Goleiro(assets[GOLEIRO_IMAGE], 480, 452)
                all_goleiros.add(goleiro)
                all_sprites.add(goleiro)
                bola = Bola(assets[BOLA_IMAGE], 480, 620)
                all_bolas.add(bola)
                all_sprites.add(bola)
                

        elif bola.profundidade == 0:
            if pos_x > 265 and pos_x < 685 and pos_y > 260 and pos_y < 440:
                placar_visitante += 1
                
                bola.kill()
                goleiro.kill()
                goleiro = Goleiro(assets[GOLEIRO_IMAGE], 480, 452)
                all_goleiros.add(goleiro)
                all_sprites.add(goleiro)
                bola = Bola(assets[BOLA_IMAGE], 480, 620)
                all_bolas.add(bola)
                all_sprites.add(bola)


            else:
                bola.kill()
                goleiro.kill()
                goleiro = Goleiro(assets[GOLEIRO_IMAGE], 480, 452)
                all_goleiros.add(goleiro)
                all_sprites.add(goleiro)
                bola = Bola(assets[BOLA_IMAGE], 480, 620)
                all_bolas.add(bola)
                all_sprites.add(bola)

        #all_sprites.update()
        # ----- Gera saidas
        window.fill((255, 255, 255))  # Preenche com a cor branca
        window.blit(assets[GAME_BACKGROUND], (0, 0))
        if time_casa == 'PSG':
            window.blit(assets[PSG_IMAGE], (80, 20))
        elif time_casa == 'MAN':
            window.blit(assets[MANCHESTER_IMAGE], (80, 20)) 
        elif time_casa == 'RMA':
            window.blit(assets[REALMADRID_IMAGE], (80, 20)) 
        elif time_casa == 'FCB':
            window.blit(assets[BAYERN_IMAGE], (80, 20)) 

        if time_rival == 'PSG':
            window.blit(assets[PSG_IMAGE], (830, 20))
        elif time_rival == 'MAN':
            window.blit(assets[MANCHESTER_IMAGE], (830, 20)) 
        elif time_rival == 'RMA':
            window.blit(assets[REALMADRID_IMAGE], (830, 20)) 
        elif time_rival == 'FCB':
            window.blit(assets[BAYERN_IMAGE], (830, 20)) 

        all_sprites.draw(window)
        cor = (255, 0, 0)
        font = pygame.font.SysFont(None, 48)
        score = font.render('{0} {1} x {2} {3}'.format(time_casa, placar_casa, placar_visitante, time_rival), True, (255, 255, 255))
        score_rect = score.get_rect()
        score_rect.midtop = (WIDTH / 2,  50)
        window.blit(score, score_rect)
        round = font.render('Rodada {0}'.format(rodadas), True, (255, 255, 255))
        round_rect = round.get_rect()
        round_rect.midtop = (WIDTH / 2,  10)
        window.blit(round, round_rect)

    
        pygame.display.update()  # Mostra o novo frame para o jogador

    return status, rodadas, placar_casa, placar_visitante
