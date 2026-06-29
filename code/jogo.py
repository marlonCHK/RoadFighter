import pygame
from code.Player import Player
from code.Entity_factory import EntityFactory
from code.Menu import Menu
from code.Level import Level
from code.Game_over import Game_over

class Jogo:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))


    def iniciar(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.iniciar()

            if menu_return == 0:
                level = Level(self.window, 'Level1')
                game_over = level.iniciar()

                if game_over:
                    tela = Game_over(self.window)
                    tela.iniciar()
            else:
                pygame.quit()
                quit()
