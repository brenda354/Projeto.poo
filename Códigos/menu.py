import pygame
import sys

# --------- Configurações ---------
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 400
FPS = 60

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (90, 23, 25)

pygame.init()
pygame.display.set_caption("Menu Inicial - Paciente Zero")

pygame.mixer.music.set_volume(0.05)
Musica_de_fundo = pygame.mixer.music.load('Músicas/Músicas_Abertura.mp3')
pygame.mixer.music.play(-1)


FONT = pygame.font.Font('Font_letra/PeaberryBase.ttf.', 32)

imagem_fundo = pygame.image.load('City 2/City2_pale.png')
imagem_fundo = pygame.transform.scale(imagem_fundo,(SCREEN_WIDTH, SCREEN_HEIGHT))


class Button:
    def __init__(self, text, pos, callback):
        self.text = text
        self.callback = callback
        self.default_color = WHITE
        self.highlight_color = HIGHLIGHT
        self.label = FONT.render(self.text, True, self.default_color)
        self.rect = self.label.get_rect(center=pos)

    def draw(self, surface, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            label = FONT.render(self.text, True, self.highlight_color)
        else:
            label = self.label
        surface.blit(label, self.rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.callback()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        mid_x = SCREEN_WIDTH // 2
        start_y = SCREEN_HEIGHT // 2 - 50
        gap = 60

        self.buttons = [
            Button("Iniciar", (mid_x, start_y), self.start_game),
            Button("Configurações",  (mid_x, start_y + gap), self.show_options),
            Button("Sair",   (mid_x, start_y + 2*gap), self.exit_game),
        ]
        
        self.running = True
    def start_game(self):
        print("Iniciando o jogo...")  
        self.running = False

    def show_options(self):
        print("Abrindo opções...")  
       

    def exit_game(self):
        pygame.quit()
        sys.exit()
    
    def adicionar_imagem(self):
        imagem_fundo = pygame.transform.scale(imagem_fundo,(SCREEN_WIDTH, SCREEN_WIDTH))

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            font_titulo = pygame.font.Font('Font_letra/PeaberryBase.ttf.', 75)  
            texto_titulo = font_titulo.render("Paciente Zero", True, (255, 255, 255)) 
            rect_titulo = texto_titulo.get_rect(center=(SCREEN_WIDTH // 2, 80)) 

            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for btn in self.buttons:
                        btn.check_click(mouse_pos)

            self.screen.blit(imagem_fundo, (0,0))
            self.screen.blit(texto_titulo, rect_titulo)

            for btn in self.buttons:
                btn.draw(self.screen, mouse_pos)

            pygame.display.flip()
            clock.tick(FPS)
        

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    def run(self):
        menu = Menu(self.screen)
        menu.run()
       
        self.game_loop()

    def game_loop(self):
        
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((30, 30, 30))
           
        pygame.display.flip()
        clock.tick(FPS)
        pygame.quit()


if __name__ == "__main__":
    Game().run()