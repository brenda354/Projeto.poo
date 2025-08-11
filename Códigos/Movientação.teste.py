import pygame 
from pygame.locals import *
from sys import exit

pygame.init()

pygame.mixer.music.set_volume(0.05)
Musica_de_fundo = pygame.mixer.music.load('Músicas/Trilha do jogo.mp3')
pygame.mixer.music.play(-1)


largura =  840
altura = 400

PETRO = (0,0,0)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Paciente Zero")

class Zumbi(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (1).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (2).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (3).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (4).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (5).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (6).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (7).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (8).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (9).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (10).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (11).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (12).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (13).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (14).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (15).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (16).png'))
        self.sprites.append(pygame.image.load('sprite_0/sprite_Zumbi (17).png'))

        self.atual = 0
        self.image = self.sprites[self.atual] 

        self.rect = self.image.get_rect()
        self.rect.topleft = 40, 290

        self.pos_y_inicial = 290
        self.pulo = False

    def pular(self):
        self.pulo = True

    def update(self):
        if self.pulo == True:
            if self.rect.y <= 200:
                self.pulo = False
            self.rect.y -= 20
        else: 
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 30
            else:
                self.rect.y = self.pos_y_inicial

        self.atual = self.atual + 0.20
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (322 * 3, 128 * 3)) 
    

todas_as_sprites = pygame.sprite.Group() 
zumbi = Zumbi()
todas_as_sprites.add(zumbi)

imagem_fundo = pygame.image.load('City 2/City2_pale.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo,(largura, altura))

relogio = pygame.time.Clock()

while True:
    relogio.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
        if event.type == KEYDOWN:
           if event.key == K_SPACE:
             if zumbi.rect.y != zumbi.pos_y_inicial:
                 pass
             else:
              zumbi.pular()

    tela.blit(imagem_fundo, (0,0))
    todas_as_sprites.draw(tela) 
    todas_as_sprites.update()
    pygame.display.flip()
