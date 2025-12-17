import pygame
import random

class Fundo:
    def __init__(self, tela, largura, altura):
        self.tela = tela
        self.largura = largura
        self.altura = altura
        self.estrelas = []
        
        for velocidade, quantidade in [(1, 80), (2, 60), (3, 40)]:
            for _ in range(quantidade):
                self.estrelas.append([random.randint(0, self.largura), random.randint(0, self.altura), velocidade])

        self.imagemfundo = pygame.image.load(
            "Sprites/Galáxia.png"
        ).convert_alpha()

        self.imagem = pygame.transform.scale(
            self.imagemfundo, (self.largura, self.altura)
        )

        pygame.mixer.init()
        pygame.mixer.music.load("HappyWorldWithMochi - With you [Pop_Electro].mp3")
        pygame.mixer.music.set_volume(0.20)
        pygame.mixer.music.play (-1)

    def desenhar(self):
        self.tela.blit(self.imagem, (0, 0))

        for e in self.estrelas:
            e[1] += e[2]
            if e[1] > self.altura:
                e[1] = 0
                e[0] = random.randint(0, self.largura)

            brilho = 120 + e[2] * 20
            pygame.draw.circle(self.tela, (brilho, brilho, brilho), (e[0], e[1]), 1)
    














