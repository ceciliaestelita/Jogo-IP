import pygame
import sys
from Objetos.Nave import Nave
from Aspectos.FundoJogo import Fundo
from Objetos.Asteroides import Asteroide
from Tela.Telainicial import Mostrar_tela_inicial
from Tela.TelaGameOver import Game_Over
from Objetos.Coletáveis.Estrela import Estrela
from Objetos.Coletáveis.c3po import C3PO
from Objetos.Coletáveis.r2d2 import R2D2
# ---------------------------------------------------------------------------
pygame.init()
info = pygame.display.Info()
LARGURA = info.current_w
ALTURA = info.current_h

tela = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption("Em uma galáxia muito muito distante")

Mostrar_tela_inicial(tela, LARGURA, ALTURA)
# ---------------------------------------------------------------------------
# Sons
som_impacto = pygame.mixer.Sound("Sons/Impacto.wav")
som_estrela_obtida = pygame.mixer.Sound("Sons/Estrelasom.mp3")
C3PO_obtido = pygame.mixer.Sound("Sons/C3POsom.mp3")
# ---------------------------------------------------------------------------
# Chamada do fundo e da nave
fundo = Fundo(tela, LARGURA, ALTURA)
nave = Nave(LARGURA // 2, ALTURA)
# ---------------------------------------------------------------------------
# Grupos
grupo_nave = pygame.sprite.Group(nave)
grupo_tiros = pygame.sprite.Group()
Grupoasteroides = pygame.sprite.Group()
grupo_estrela = pygame.sprite.Group()
grupo_c3po = pygame.sprite.Group()
grupo_r2d2 = pygame.sprite.Group()
# ---------------------------------------------------------------------------
TempoAsteroide = pygame.USEREVENT + 1
pygame.time.set_timer(TempoAsteroide, 500)

TempoEstrela = pygame.USEREVENT + 2
pygame.time.set_timer(TempoEstrela, 1000)

TempoC3PO = pygame.USEREVENT + 3
pygame.time.set_timer(TempoC3PO, 5000)

TempoR2D2 = pygame.USEREVENT + 4
pygame.time.set_timer(TempoR2D2, 7000)
# ---------------------------------------------------------------------------
quantidade_estrelas = 0
quantidade_c3po = 0
quantidade_r2d2 = 0
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
        if event.type == TempoEstrela:
            nova_estrela = Estrela(LARGURA, ALTURA, tela)
            grupo_estrela.add(nova_estrela)
        if event.type == TempoC3PO:
            nova_c3po = C3PO(LARGURA, ALTURA, tela)
            grupo_c3po.add(nova_c3po)
        if event.type == TempoR2D2:
            nova_r2d2 = R2D2(LARGURA, ALTURA, tela)
            grupo_r2d2.add(nova_r2d2)
    # ---------------------------------------------- 
    fundo.desenhar()
    grupo_nave.draw(tela)
    grupo_tiros.draw(tela)
    Grupoasteroides.draw(tela)
    grupo_estrela.draw(tela)
    grupo_c3po.draw(tela)
    grupo_r2d2.draw(tela)
    # ---------------------------------------------- 
    fonte = pygame.font.Font(None, 36)
    texto_estrelas = fonte.render(f"Estrelas: {quantidade_estrelas}", True, (255, 255, 255))
    texto_c3po = fonte.render(f"C3PO: {quantidade_c3po}", True, (255, 255, 0))
    texto_r2d2 = fonte.render(f"R2D2: {quantidade_r2d2}", True, (0, 255, 255))
    tela.blit(texto_c3po, (10, 50))
    tela.blit(texto_r2d2, (10, 90))
    tela.blit(texto_estrelas, (10, 10))
    # ------------------------------------------------------
    teclas = pygame.key.get_pressed()
    grupo_nave.update(teclas)
    grupo_tiros.update()
    Grupoasteroides.update()
    grupo_estrela.update()
    grupo_c3po.update()
    grupo_r2d2.update()

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
    # ----------------------------------------------
    # Colisão nave x estrela ---
    colisoes_estrela = pygame.sprite.spritecollide(nave, grupo_estrela, True)
    for estrela in colisoes_estrela:
        estrela.kill() # Remove a estrela da tela
        quantidade_estrelas += 1 # Incrementa o contador
        som_estrela_obtida.play()
    # ----- x -------
    # Colisão nave x c3po ---
    colisoes_c3po = pygame.sprite.spritecollide(nave, grupo_c3po, True)
    for c3po in colisoes_c3po:
        c3po.kill() # Remove o c3po da tela
        quantidade_c3po += 1 # Incrementa o contador
        C3PO_obtido.play()
    # ----- x -------
    # Colisão nave x estrela ---
    colisoes_r2d2 = pygame.sprite.spritecollide(nave, grupo_r2d2, True)
    for r2d2 in colisoes_r2d2:
        r2d2.kill() # Remove o r2d2 da tela
        quantidade_r2d2 += 1 # Incrementa o contador
    # ----- x -------
    # Colisão nave x asteroide ---
    colisoes = pygame.sprite.spritecollide(nave, Grupoasteroides, True)
    for asteroide in colisoes:
        asteroide.kill()
        pygame.mixer.music.stop()
        Game_Over(tela, LARGURA, ALTURA)
        pygame.quit()
        sys.exit()
    # ---------------------------------------------- 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


