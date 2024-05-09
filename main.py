import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# Música de fundo:
pygame.mixer.music.set_volume(0.15) # Volume da música (0 a 1).
musica_fundo = pygame.mixer.music.load('BoxCat Games - Victory.mp3')
pygame.mixer.music.play(-1)

# Efeitos sonoros:
coin_sound = pygame.mixer.Sound('smw_coin.wav')
coin_sound.set_volume(0.5) # Volume do efeito sonoro (0 a 1).

largura = 640 # eixo x
altura = 480 # eixo y
x = int(largura / 2 - 20)
y = int(altura / 2)
vel = 9

# Posição inicial do retângulo azul:
x_azul = randint(40, 600)
y_azul = randint(50, 430)

# Texto:
pontos = 0
fonte = pygame.font.SysFont('arial', 35, True, True)

# Tela:
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Mexendo o boneco')
relogio = pygame.time.Clock()

# Função para gerar posição aleatória do retângulo azul:
def randPosition():
    x_azul = randint(40, 600)
    y_azul = randint(60, 430)
    return x_azul, y_azul

# Loop principal:
while True:
    relogio.tick(60) # Controla a velocidade de ticks no jogo.
    tela.fill((0, 0, 0)) # Preenchendo a tela com a cor preta.
    mensagem = f'Pontos: {pontos}' # Mensagem que será exibida na tela.
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255)) # Formatação do texto.

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         x = x - 20
        #     if event.key == K_d:
        #         x = x + 20
        #     if event.key == K_w:
        #         y = y - 20
        #     if event.key == K_s:
        #         y = y + 20
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                x = largura / 2 - 20
                y = altura / 2

    if pygame.key.get_pressed()[K_a]:
        x = x - vel
    if pygame.key.get_pressed()[K_d]:
        x = x + vel
    if pygame.key.get_pressed()[K_w]:
        y = y - vel
    if pygame.key.get_pressed()[K_s]:
        y = y + vel

    ret_player = pygame.draw.rect(tela, (150, 10, 200), (x, y, 40, 60))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 60))

    if ret_player.colliderect(ret_azul):
        x_azul, y_azul = randPosition()
        pontos += 1
        coin_sound.play() # Tocando o som de moeda.

    tela.blit(texto_formatado, (450, 40)) # Exibindo o texto na tela.

    pygame.display.update()