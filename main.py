from tkinter import Y
import pygame

class Bola(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 10
    
    def update(self):
        self.rect.centerx += self.speedx
        self.rect.centery += 2

pygame.init()

WIDTH = 960
HEIGHT = 720
BOLA_WIDTH = 80
BOLA_HEIGHT = 80
window = pygame.display.set_mode((WIDTH, HEIGHT))

game = True

# ----- Inicia assets
image = pygame.image.load('Tela_inicial.png').convert()
image = pygame.transform.scale(image, (960, 720)) #acertar a escala certa da imagem de mudar a width e height se necessario
bola_imagem = pygame.image.load('Bola_de_futebol.png').convert_alpha()
bola_imagem = pygame.transform.scale(bola_imagem, (BOLA_WIDTH, BOLA_HEIGHT))



#bola_x = 200
# y negativo significa que está acima do topo da janela. O meteoro começa fora da janela
#bola_y = -BOLA_HEIGHT
#bola_speedx = 3
#bola_speedy = 4
clock = pygame.time.Clock()
FPS = 30

# ===== Loop principal =====
INICIAL = 1
QUIT = 0
GAME = 2
status = INICIAL
bola = None
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
                status = GAME

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(image, (0, 0))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    while status == GAME:
        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = QUIT

        if bola == None:
            bola = Bola(bola_imagem, 50, 30)
            all_sprites.add(bola)

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
        # window.blit(image, (0, 0))

        all_sprites.draw(window)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

