import pygame

class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(
            "Novojogo.py/Sprites/Tiro.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(self.image, (60, 90))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

        self.velocidade = -10  # sobe

    def update(self):
        self.rect.y += self.velocidade

        if self.rect.bottom < 0:
            self.kill()
