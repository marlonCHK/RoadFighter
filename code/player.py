import pygame

class Player:
    def __init__(self):
        spritesheet = pygame.image.load('./assets/Idle.png').convert_alpha()

        self.image = spritesheet.subsurface((0,0,128,128))
        self.rect = self.image.get_rect(center=(288, 210))

    def atacar_esq(self):
        """
        Ataca inimigos vindos da esquerda.
        """
        print("Ataque para a esquerda")

    def atacar_dir(self):
        """
        Ataca inimigos vindos da direita.
        """
        print("Ataque para a direita")