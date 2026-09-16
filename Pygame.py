import pygame
import random

# Inicialização
pygame.init()

# Tela
LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cai-Desvia")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 100, 255)
PRETO = (0, 0, 0)

# Jogador
jogador_x = 350
jogador_y = 520
jogador_largura = 80
jogador_altura = 20
velocidade_jogador = 8

# Obstáculo
obst_x = random.randint(0, LARGURA - 50)
obst_y = -50
obst_largura = 50
obst_altura = 50
velocidade_obst = 5

# Fonte
fonte = pygame.font.SysFont(None, 40)

pontuacao = 0

clock = pygame.time.Clock()

rodando = True

while rodando:

    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jogador_x -= velocidade_jogador

    if teclas[pygame.K_RIGHT]:
        jogador_x += velocidade_jogador

    # Limites da tela
    if jogador_x < 0:
        jogador_x = 0

    if jogador_x > LARGURA - jogador_largura:
        jogador_x = LARGURA - jogador_largura

    # Queda do obstáculo
    obst_y += velocidade_obst

    if obst_y > ALTURA:
        obst_y = -50
        obst_x = random.randint(0, LARGURA - 50)
        pontuacao += 1

    # Retângulos para colisão
    jogador = pygame.Rect(
        jogador_x,
        jogador_y,
        jogador_largura,
        jogador_altura
    )

    obstaculo = pygame.Rect(
        obst_x,
        obst_y,
        obst_largura,
        obst_altura
    )

    # Colisão
    if jogador.colliderect(obstaculo):
        print("Game Over!")
        rodando = False

    # Desenho
    tela.fill(BRANCO)

    pygame.draw.rect(tela, AZUL, jogador)
    pygame.draw.rect(tela, VERMELHO, obstaculo)

    texto = fonte.render(
        f"Pontuação: {pontuacao}",
        True,
        PRETO
    )

    tela.blit(texto, (10, 10))

    pygame.display.update()

pygame.quit()