import pygame
from config import *

INICIAL_BACKGROUND = 'inicial.background'
TIME_BACKGROUND = 'time.background'
BOLA_IMAGE = 'bola.image'
GAME_BACKGROUND = 'game.background'
GOLEIRO_IMAGE = 'goleiro.image'
CHUTEIRA_IMAGE = 'chuteira.image'
GOL_IMAGE = 'gol.image'
TEXTO = 'selecionepais.txt'
BAYERN_IMAGE = 'iconebayern.image'
PSG_IMAGE = 'iconepsg.image'
MANCHESTER_IMAGE = 'iconemanchester.image'
REALMADRID_IMAGE = 'iconerealmadrid.image'
TELA_AVISO_CHUTE = 'avisochute.image'
TELA_AVISO_DEFESA = 'avisodefesa.image'
FIM_BACKGROUND = 'telafinal.background'
CHAMPIONS_MUSICA = 'champions.mp3'

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
    a[TIME_BACKGROUND] = pygame.image.load('Escolha_dos_times.png').convert_alpha()
    a[TIME_BACKGROUND] = pygame.transform.scale(a[TIME_BACKGROUND], (960, 720))
    
    a[GOL_IMAGE] = pygame.image.load('gol.png').convert_alpha()
    a[GOL_IMAGE] = pygame.transform.scale(a[GOL_IMAGE], (680, 720))
    a[TEXTO] = pygame.font.SysFont(None, 48)
    a[TEXTO] = a[TEXTO].render('Selecione um país para jogar', True, (255, 0, 0))

    a[BAYERN_IMAGE] = pygame.image.load('bayern.png').convert_alpha()
    a[BAYERN_IMAGE] = pygame.transform.scale(a[BAYERN_IMAGE], (80, 80))

    a[PSG_IMAGE] = pygame.image.load('Psg.png').convert_alpha()
    a[PSG_IMAGE] = pygame.transform.scale(a[PSG_IMAGE], (140, 90))

    a[MANCHESTER_IMAGE] = pygame.image.load('ManU.png').convert_alpha()
    a[MANCHESTER_IMAGE] = pygame.transform.scale(a[MANCHESTER_IMAGE], (70, 70))

    a[REALMADRID_IMAGE] = pygame.image.load('RealM.png').convert_alpha()
    a[REALMADRID_IMAGE] = pygame.transform.scale(a[REALMADRID_IMAGE], (80, 80))

    a[TELA_AVISO_CHUTE] = pygame.image.load('Imagem_chutar_aviso.png').convert_alpha()
    a[TELA_AVISO_CHUTE] = pygame.transform.scale(a[TELA_AVISO_CHUTE], (960, 720))
    a[TELA_AVISO_DEFESA] = pygame.image.load('Imagem_defender_aviso.png').convert_alpha()
    a[TELA_AVISO_DEFESA] = pygame.transform.scale(a[TELA_AVISO_DEFESA], (960, 720))

    a[FIM_BACKGROUND] = pygame.image.load('Imagem_final_de_jogo.png').convert_alpha()
    a[FIM_BACKGROUND] = pygame.transform.scale(a[FIM_BACKGROUND], (960, 720))
    

    a[CHAMPIONS_MUSICA] = pygame.mixer.music.load('hino_champions.mp3')
    a[CHAMPIONS_MUSICA] = pygame.mixer.music.set_volume(0.4)
    #assets[] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    return a


