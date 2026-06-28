import random
from code.Inimigo import Inimigo


class EntityFactory:

    @staticmethod
    def criar_inimigo(velocidade):

        lado = random.choice(["esquerda", "direita"])

        return Inimigo(
            direcao=lado,
            velocidade=velocidade
        )