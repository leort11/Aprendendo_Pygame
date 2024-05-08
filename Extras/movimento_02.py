import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2
meio = largura/2 - 20 # Meio para o objeto retangulo:

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Movimento')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30) # Controla a velocidade de ticks no jogo.
    tela.fill((0, 0, 0)) 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (0, 50, 255), (meio, y, 40, 60))
    pygame.draw.circle(tela, (255, 0, 0), (x, y), 40)

    # Comando para quando o objeto chegar na posição y >= ao tamanho da tela, volte para o topo. 
    if y >= altura:
        y = 0


    y = y + 1

    pygame.display.update()