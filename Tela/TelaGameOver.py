import pygame
import sys

def Game_Over(tela, largura, altura):
    tela_img = pygame.image.load("Sprites/TelaGameOver.jpg").convert()
    tela_img = pygame.transform.scale(tela_img, (largura, altura))

    clock = pygame.time.Clock()

    while True:  # Loop infinito até o jogador apertar algo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Qualquer tecla fecha o jogo
                pygame.quit()
                sys.exit()

        tela.blit(tela_img, (0, 0))
        pygame.display.flip()
        clock.tick(60)
