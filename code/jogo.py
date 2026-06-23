import random

from player import Player
from inimigo import Inimigo


class Jogo:
    def __init__(self):
        self.player = Player()
        self.inimigos = []

        self.score = 0
        self.velocidade = 1.0
        self.rodando = True

        self.tempo_sobrevivencia = 0

    def iniciar(self):
        """
        Inicia a partida.
        """
        self.rodando = True
        self.score = 0
        self.velocidade = 1.0
        self.inimigos.clear()

        print("Partida iniciada")

    def atualizar(self):
        """
        Atualiza o estado do jogo.
        """
        for inimigo in self.inimigos:
            inimigo.mover()

        self.verificar_colisao()

    def gerar_inimigo(self):
        """
        Cria inimigos à esquerda ou à direita.
        """
        lado = random.choice(["esquerda", "direita"])

        if lado == "esquerda":
            posicao = -100
        else:
            posicao = 100

        inimigo = Inimigo(
            posicao_x=posicao,
            direcao=lado,
            velocidade=self.velocidade
        )

        self.inimigos.append(inimigo)

    def aumentar_dificuldade(self):
        """
        Aumenta a velocidade dos inimigos.
        """
        self.velocidade += 0.2

    def verificar_colisao(self):
        """
        Verifica se algum inimigo alcançou o jogador.
        """
        for inimigo in self.inimigos:
            if inimigo.atingir_player(self.player.posicao_x):
                self.game_over()

    def game_over(self):
        """
        Finaliza a partida.
        """
        self.rodando = False
        print("GAME OVER")