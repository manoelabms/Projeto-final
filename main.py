from tkinter import Y
import pygame
pygame.init()

class Bola(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 1

    def update(self):

        self.rect.centerx += self.speedx
        self.rect.centery += -2

        if self.rect.right < WIDTH:
            self.rect.right = 480
        if self.rect.left > HEIGHT:
            self.rect.left = 720

class Goleiro(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0

WIDTH = 960
HEIGHT = 720
BOLA_WIDTH = 80
BOLA_HEIGHT = 80
GOLEIRO_WIDTH = 160
GOLEIRO_HEIGHT = 210
window = pygame.display.set_mode((WIDTH, HEIGHT))

game = True

# ----- Inicia assets
image = pygame.image.load('Tela_inicial.png').convert()
image = pygame.transform.scale(image, (960, 720)) #acertar a escala certa da imagem de mudar a width e height se necessario
bola_imagem = pygame.image.load('Bola_de_futebol.png').convert_alpha()
bola_imagem = pygame.transform.scale(bola_imagem, (BOLA_WIDTH, BOLA_HEIGHT))
game_imagem = pygame.image.load('Imagem_jogo.jpg').convert_alpha()
game_imagem = pygame.transform.scale(game_imagem, (960, 720))
goleiro_imagem = pygame.image.load('Goleiro_.png').convert_alpha()
goleiro_imagem = pygame.transform.scale(goleiro_imagem, (GOLEIRO_WIDTH, GOLEIRO_HEIGHT))
times_imagem = pygame.image.load('Escolha_dos_times.jpg').convert_alpha()
times_imagem = pygame.transform.scale(times_imagem, (960, 720))


clock = pygame.time.Clock()
FPS = 30

# ===== Loop principal =====
INICIAL = 1
QUIT = 0
TIMES = 3
GAME = 2
status = INICIAL
bola = None
goleiro = None
all_sprites = pygame.sprite.Group()

while status != QUIT:
    # ----- Trata eventos
    while status == INICIAL:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT
            # ----- Verifica consequências
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = TIMES

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(image, (0, 0))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    while status == TIMES:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT

            if event.type == pygame.MOUSEBUTTONDOWN:
                status = GAME
        window.fill((255, 255, 255))  # Preenche com a cor branca
        window.blit(times_imagem, (0, 0))

        # ----- Atualiza estado do jogo
        pygame.display.update()

    while status == GAME:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT

        if bola == None:
            bola = Bola(bola_imagem, 480,720)
            all_sprites.add(bola)

        if goleiro == None:
            goleiro = Goleiro(goleiro_imagem, 480, 560)
            all_sprites.add(goleiro)
        
        all_sprites.update()

        # ----- Atualiza estado do jogo
        # Atualizando a posição da bola
        #bola_x += bola_speedx
        #bola_y += bola_speedy
        # Se a bola passar do final da tela, volta para cima
        #if bola_y > HEIGHT or bola_x + BOLA_WIDTH < 0 or bola_x > WIDTH:
            #bola_x = 200
            #bola_y = -BOLA_HEIGHT

        # ----- Gera saídas
        window.fill((255, 255, 255))  # Preenche com a cor branca
        window.blit(game_imagem, (0, 0))

        all_sprites.draw(window)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    



# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

