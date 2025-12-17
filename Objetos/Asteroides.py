import pygame
import random

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, largura_tela, altura_tela, tela):
        super().__init__()
        
        self.image = pygame.image.load(
            "Sprites/Asteroide.png"
        ).convert_alpha()

        tamanhos = ["pequeno", "medio", "grande"]
        pesos = [0.7, 0.2, 0.1] 
        self.tamanho = random.choices(tamanhos, pesos)[0]

        if self.tamanho == "pequeno":
            tamanho_px = 120
            self.vida = 1
        elif self.tamanho == "medio":
            tamanho_px = 180
            self.vida = 2
        else:  # grande
            tamanho_px = 240
            self.vida = 3

        self.image = pygame.transform.scale(self.image, (tamanho_px, tamanho_px))

        self.rect = self.image.get_rect()

        # Posição inicial aleatória no topo
        self.rect.x = random.randint(0, largura_tela - self.rect.width)
        self.rect.y = random.randint(-100, -40)

        # Movimento
        if self.tamanho == "pequeno":
            self.vel = random.uniform(12, 14)
        elif self.tamanho == "medio":
            self.vel = random.uniform(5.6, 7.4)
        else:  # grande
            self.vel = random.uniform(4, 4.9)

        self.altura_tela = altura_tela
        self.tela = tela

    def update(self):
        self.rect.y += self.vel

    def desenhar(self):
        self.tela.blit(self.image, self.rect)

    def fora_da_tela(self):
        return self.rect.top > self.altura_tela






