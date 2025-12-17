import pygame
import random

class C3PO(pygame.sprite.Sprite):
    tamanho_px = 130
    def __init__(self, largura_tela, altura_tela, tela):
        super().__init__()

        # Carrega a sprite 
        self.image = pygame.image.load(
            "Sprites/c3po.png"
        ).convert_alpha()

        
        self.vida = 1
        
        self.image = pygame.transform.scale(self.image, (self.tamanho_px, self.tamanho_px))

        self.rect = self.image.get_rect()

        # Posição inicial aleatória no topo
        self.rect.x = random.randint(0, largura_tela - self.rect.width)
        self.rect.y = random.randint(-100, -40)

        # Movimento
        
        self.vel = random.uniform(5.6, 7.4)
        
        self.altura_tela = altura_tela
        self.tela = tela

    def update(self):
        self.rect.y += self.vel

    def desenhar(self):
        self.tela.blit(self.image, self.rect)

    def fora_da_tela(self):
        return self.rect.top > self.altura_tela



