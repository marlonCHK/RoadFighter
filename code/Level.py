import pygame
from code.Entity_factory import EntityFactory
from code.Player import Player

class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name

        self.background = pygame.image.load("./assets/level1bg.png").convert()
        self.background_rect = self.background.get_rect()

        self.player = Player()
        self.enemy_list = []
        self.enemy_list.append(
            EntityFactory.criar_inimigo(3)
        )

    def iniciar(self):
        pygame.mixer.music.load('./assets/at_the_end_of_hope_intro.wav')
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            self.window.blit(self.background, (0, 0))
            self.window.blit(self.player.image, self.player.rect)

            for enemy in self.enemy_list:
                enemy.atualizar()
                self.window.blit(enemy.image, enemy.rect)

            pygame.display.flip()