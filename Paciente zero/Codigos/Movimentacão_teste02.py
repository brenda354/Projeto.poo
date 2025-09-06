import pygame
from pygame.locals import *
from sys import exit 
import os

pygame.init()

pasta = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta, '..', 'SpriteSheet')
pasta_sons = os.path.join(pasta, 'Musicas')

caminho_sprite = os.path.join(pasta_imagens, 'Zumbi.png')
print("Caminho da imagem:", caminho_sprite)

LARGURA = 840
ALTURA = 600
BRANCO = (255, 255, 255)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Paciente zero')

sprit_zumbi = pygame.image.load(caminho_sprite).convert_alpha()

class Zumbi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagens_zumbi = []
        for i in range(8):
            img = sprit_zumbi.subsurface((i * 32, 0), (32, 33))
            img = pygame.transform.scale(img, (33 * 3 , 33 * 3))
            self.imagens_zumbi.append(img)

        self.index_lista = 0
        self.image = self.imagens_zumbi[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 460)
    
    def update(self):
        if self.index_lista > 7:
            self.index_lista = 0 
        self.index_lista += 0.25
        self.image = self.imagens_zumbi[int(self.index_lista)]

        

todas_as_sprites = pygame.sprite.Group()
zumbi = Zumbi()
todas_as_sprites.add(zumbi)

relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    todas_as_sprites.update()
    todas_as_sprites.draw(tela)
    pygame.display.flip()
