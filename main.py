import pygame

pygame.init()

WIDTH = 960
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

game = True

# ----- Inicia assets
image = pygame.image.load('Tela_inicial.png').convert()
image = pygame.transform.scale(image, (960, 720)) 

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (0, 0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

