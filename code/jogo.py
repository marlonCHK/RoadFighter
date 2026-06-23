from code.player import Player
from code.entity_factory import EntityFactory


class Jogo:

    def __init__(self):

        self.player = Player()

        self.inimigos = []

        self.score = 0

        self.velocidade = 1.0

        self.tempo_sobrevivencia = 0

        self.rodando = False

    def iniciar(self):

        self.score = 0

        self.velocidade = 1.0

        self.tempo_sobrevivencia = 0

        self.inimigos.clear()

        self.rodando = True

        print("Partida iniciada")

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