# Imports: pygame, sys.
import pygame
from pygame.locals import *
from sys import exit # Importando a função exit que encerra o programa quando a janela é fechada.

pygame.init() # Inicializando o pygame.

largura = 640 # eixo x
altura = 480 # eixo y
verde = (30, 200, 75)
rosa = (255, 0, 150)

tela = pygame.display.set_mode((largura, altura)) # Criando a tela.
pygame.display.set_caption('Jogo') # Titulo da janela.

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, rosa, (200, 300, 100, 50))
    pygame.draw.circle(tela, verde, (250, 260), 40)
    pygame.draw.line(tela, (255, 255, 255), (390, 0), (390, 600), 10)

    pygame.display.update() # Atualizando a tela do jogo.