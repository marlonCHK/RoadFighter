import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Summer2.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def iniciar(self):
        menu_option = 0
        pygame.mixer.music.load('./assets/awesomeness.wav')
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Road", (149, 6, 6), ((576/2), 70))
            self.menu_text(60, "Fighter", (149, 6, 6), ((576/2), 120))
            
            if menu_option == 1:
                self.menu_text(40, "Play", (73, 76, 78), ((576/2), 200))
                self.menu_text(40, "Exit", (136, 8, 8), ((576/2), 240))
            else:
                self.menu_text(40, "Play", (136, 8, 8), ((576/2), 200))
                self.menu_text(40, "Exit", (73, 76, 78), ((576/2), 240))
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Close Window
                    quit() #endpygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = 1 
                    if event.key == pygame.K_RETURN:
                        return menu_option
            

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
