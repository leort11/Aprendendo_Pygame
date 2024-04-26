import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640 # eixo x
altura = 480 # eixo y
x = largura / 2
y = altura / 2

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Mexendo o boneco')
relogio = pygame.time.Clock()

while True:
    relogio.tick(50) # Controla a velocidade de ticks no jogo.
    tela.fill((0, 0, 0)) # Preenchendo a tela com a cor preta.

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20

    pygame.draw.rect(tela, (150, 10, 200), (x, y, 40, 60))

    pygame.display.update()