import pygame
import sys

def Mostrar_tela_inicial(tela, largura, altura):
    """Mostra a tela inicial até o jogador apertar ENTER"""
    tela_inicial_img = pygame.image.load("Sprites/TelaInicial.jpeg").convert()
    tela_inicial_img = pygame.transform.scale(tela_inicial_img, (largura, altura))

    esperando = True
    clock = pygame.time.Clock()

    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter para iniciar
                    esperando = False

        tela.blit(tela_inicial_img, (0, 0))
        pygame.display.flip()
        clock.tick(60)



