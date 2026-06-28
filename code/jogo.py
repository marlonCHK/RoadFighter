import pygame
from code.Player import Player
from code.Entity_factory import EntityFactory
from code.Menu import Menu
from code.Level import Level

class Jogo:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))
        
        #self.player = Player()
        #self.inimigos = []
        #self.score = 0
        #self.velocidade = 1.0
        #self.tempo_sobrevivencia = 0
        #self.rodando = False

    def iniciar(self):
        #self.score = 0
        #self.velocidade = 1.0
        #self.tempo_sobrevivencia = 0
        #self.inimigos.clear()
        #self.rodando = True

        while True:
            menu = Menu(self.window)
            menu_return = menu.iniciar()

            if menu_return == 0:
                level = Level(self.window, 'Level1')
                level.iniciar()
            else:
                pygame.quit()
                quit()
            
           


    def atualizar(self):

        for inimigo in self.inimigos:
            inimigo.mover()

        self.verificar_colisao()

    def gerar_inimigo(self):

        inimigo = EntityFactory.criar_inimigo(
            self.velocidade
        )

        self.inimigos.append(inimigo)

    def aumentar_dificuldade(self):

        self.velocidade += 0.2

    def verificar_colisao(self):

        for inimigo in self.inimigos:

            if inimigo.atingir_player(
                self.player.posicao_x
            ):
                self.game_over()

    def game_over(self):

        self.rodando = False

        print("GAME OVER")