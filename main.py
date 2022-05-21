import pygame

pygame.init()

WIDTH = 960
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

game = True

# ----- Inicia assets
<<<<<<< HEAD
image = pygame.image.load('tela_inicio_pygame.jpeg').convert()
image = pygame.transform.scale(image, (960, 720))
=======
image = pygame.image.load('Tela_inicial.png').convert()
image = pygame.transform.scale(image, (960, 720)) #acertar a escala certa da imagem de mudar a width e height se necessario
>>>>>>> 84e678374bb8be762eebddea844463c3aefc431f

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

