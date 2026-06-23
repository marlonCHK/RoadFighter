import random

from code.Inimigo import Inimigo


class EntityFactory:

    @staticmethod
    def criar_inimigo(velocidade):

        lado = random.choice(
            ["esquerda", "direita"]
        )

        if lado == "esquerda":
            posicao = -100
        else:
            posicao = 100

        return Inimigo(
            posicao_x=posicao,
            direcao=lado,
            velocidade=velocidade
        )