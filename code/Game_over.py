import pygame
from pygame import Surface, Rect
from pygame.font import Font


class Game_over:

    def __init__(self, window):

        self.window = window

        self.background = pygame.image.load("./assets/GameOverbg.png").convert()
        self.background_rect = self.background.get_rect()

    def iniciar(self):

        pygame.mixer.music.stop()

        while True:
            self.window.blit(self.background, self.background_rect)

            self.desenhar_texto(
                55,
                "GAME OVER",
                (180, 0, 0),
                (288, 90)
            )

            self.desenhar_texto(
                25,
                "ENTER - Voltar ao menu",
                (255, 255, 255),
                (288, 180)
            )

            self.desenhar_texto(
                25,
                "ESC - Sair",
                (255, 255, 255),
                (288, 220)
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

    def desenhar_texto(
        self,
        tamanho,
        texto,
        cor,
        posicao
    ):

        fonte: Font = pygame.font.SysFont(
            "Lucida Sans Typewriter",
            tamanho
        )

        superficie: Surface = fonte.render(
            texto,
            True,
            cor
        ).convert_alpha()

        rect: Rect = superficie.get_rect(
            center=posicao
        )

        self.window.blit(superficie, rect)