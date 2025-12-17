import pygame
import sys

def Game_Over(tela, largura, altura):
    tela_img = pygame.image.load("Sprites/TelaGameOver.jpg").convert()
    tela_img = pygame.transform.scale(tela_img, (largura, altura))

    clock = pygame.time.Clock()

    GameOver = pygame.mixer.Sound("Sons/Gameover.mp3")
    GameOver.play()

    tempo_inicio = pygame.time.get_ticks() 
    tempo_espera = 1500

    GameOverLoop = True

    while GameOverLoop:  # Loop infinito até o jogador apertar algo
        tempo_atual = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if tempo_atual - tempo_inicio > tempo_espera:
                    GameOverLoop = False
                    
        tela.blit(tela_img, (0, 0))
        pygame.display.flip()
        clock.tick(60)
