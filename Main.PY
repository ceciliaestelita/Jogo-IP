import pygame
from Objetos.Nave import Nave
from Aspectos.FundoJogo import Fundo
from Objetos.Asteroides import Asteroide
from Tela.Telainicial import Mostrar_tela_inicial
import sys

# ---------------------------------------------------------------------------
pygame.init()
info = pygame.display.Info()
LARGURA = info.current_w
ALTURA = info.current_h

tela = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption("Em uma galáxia muito muito distante")

# ---------------------------------------------------------------------------
# Sons
som_impacto = pygame.mixer.Sound("Sons/Impacto.wav")

# ---------------------------------------------------------------------------
# Chamada do fundo e da nave
fundo = Fundo(tela, LARGURA, ALTURA)
nave = Nave(LARGURA // 2, ALTURA)

# ---------------------------------------------------------------------------
# Grupos
grupo_nave = pygame.sprite.Group(nave)
grupo_tiros = pygame.sprite.Group()
Grupoasteroides = pygame.sprite.Group()

TempoAsteroide = pygame.USEREVENT + 1
pygame.time.set_timer(TempoAsteroide, 500)

# ---------------------------------------------------------------------------
# Tela inicial
Mostrar_tela_inicial(tela, LARGURA, ALTURA)

# ---------------------------------------------------------------------------
# Main loop
clock = pygame.time.Clock()
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == TempoAsteroide:
            Grupoasteroides.add(Asteroide(LARGURA, ALTURA, tela))

    fundo.desenhar()
    grupo_nave.draw(tela)
    grupo_tiros.draw(tela)
    Grupoasteroides.draw(tela)

    teclas = pygame.key.get_pressed()
    grupo_nave.update(teclas)
    grupo_tiros.update()
    Grupoasteroides.update()

    if teclas[pygame.K_SPACE]:
        nave.atirar(grupo_tiros)

    # Colisão tiro x asteroide
    colisoes = pygame.sprite.groupcollide(
        Grupoasteroides, grupo_tiros, False, True
    )
    for asteroide in colisoes:
        asteroide.vida -= 1
        som_impacto.play()
        if asteroide.vida <= 0:
            asteroide.kill()

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
