import pygame
import sys

def Game_Over(tela, largura, altura):
    Tela_Game_Over = pygame.image.load("Sprites/TelaGameOver.jpg").convert()
    Tela_Game_Over = pygame.transform.scale(Tela_Game_Over, (largura, altura))

    esperando = True
    clock = pygame.time.Clock()

    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: 
                    esperando = False

        tela.blit(Tela_Game_Over, (0, 0))
        pygame.display.flip()
        clock.tick(60)
