import pygame

pygame.init()

WIDTH = 960
HEIGHT = 720
BOLA_WIDTH = 5
BOLA_HEIGHT = 3
window = pygame.display.set_mode((WIDTH, HEIGHT))

game = True

# ----- Inicia assets
image = pygame.image.load('Tela_inicial.jpeg').convert()
image = pygame.transform.scale(image, (960, 720)) #acertar a escala certa da imagem de mudar a width e height se necessario
bola_imagem = pygame.image.load('Bola_de_futebol.png').convert_alpha()
bola_imagem_pequena = pygame.transform.scale(bola_imagem, (BOLA_WIDTH, BOLA_HEIGHT))

bola_x = 200
# y negativo significa que está acima do topo da janela. O meteoro começa fora da janela
bola_y = -BOLA_HEIGHT
bola_speedx = 3
bola_speedy = 4

# ===== Loop principal =====

while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    # ----- Atualiza estado do jogo
    # Atualizando a posição da bola
    bola_x += bola_speedx
    bola_y += bola_speedy
    # Se a bola passar do final da tela, volta para cima
    if bola_y > HEIGHT or bola_x + BOLA_WIDTH < 0 or bola_x > WIDTH:
        bola_x = 200
        bola_y = -BOLA_HEIGHT

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (0, 0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

