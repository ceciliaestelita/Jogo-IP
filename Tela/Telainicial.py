import pygame
import sys

def Mostrar_tela_inicial(tela, largura, altura):
    LyodaPODEROSOBLASTER = pygame.mixer.Sound("Sons/Lyoda.mp3")
    LyodaPODEROSOBLASTER.play()
    
    tela_inicial_img = pygame.image.load("Sprites/TelaInicial.jpeg").convert()
    tela_inicial_img = pygame.transform.scale(tela_inicial_img, (largura, altura))

    esperando = True
    clock = pygame.time.Clock()

    tempo_inicio = pygame.time.get_ticks() 
    tempo_espera = 2000

    while esperando:
        for event in pygame.event.get():
            tempo_atual = pygame.time.get_ticks()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if tempo_atual - tempo_inicio > tempo_espera:
                    esperando = False

        tela.blit(tela_inicial_img, (0, 0))
        pygame.display.flip()
        clock.tick(60)
