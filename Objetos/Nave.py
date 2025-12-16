import pygame
from Objetos.Tiro import Tiro

class Nave(pygame.sprite.Sprite):
    def __init__(self, x, altura):
        super().__init__()

        self.imagemfundo = pygame.image.load(
            "Sprites/Nave.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(self.imagemfundo, (150, 150))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, altura - 20)

        self.velocidade = 8

        self.tempo_tiro = 0
        self.delay_tiro = 300  # ms

        self.somtiro = pygame.mixer.Sound("NovoJogo.py/Sons/SomLaser.wav")

    def update(self, teclas):
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade

        largura_tela = pygame.display.get_surface().get_width()

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > largura_tela:
            self.rect.right = largura_tela

    def atirar(self, grupo_tiros):
        agora = pygame.time.get_ticks()

        if agora - self.tempo_tiro > self.delay_tiro:
            tiro = Tiro(self.rect.centerx, self.rect.top)
            grupo_tiros.add(tiro)
            self.tempo_tiro = agora
            self.somtiro.set_volume(0.2)
            self.somtiro.play()





