class Inimigo:
    def __init__(self, posicao_x, direcao, velocidade):
        self.posicao_x = posicao_x
        self.direcao = direcao
        self.velocidade = velocidade

    def mover(self):
        """
        Move o inimigo em direção ao jogador.
        """
        if self.direcao == "esquerda":
            self.posicao_x += self.velocidade
        else:
            self.posicao_x -= self.velocidade

    def atingir_player(self, posicao_player):
        """
        Verifica se atingiu o jogador.
        """
        return abs(self.posicao_x - posicao_player) <= 5