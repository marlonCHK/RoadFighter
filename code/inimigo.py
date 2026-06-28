import pygame

class Inimigo:
    def __init__(self, direcao, velocidade):
        spritesheet = pygame.image.load('./assets/Run.png').convert_alpha()

        self.frames = []

        for i in range(10):
            frame = spritesheet.subsurface((i * 128, 0, 128, 128))

            if direcao == "direita":
                frame = pygame.transform.flip(frame, True, False)

            self.frames.append(frame)
        
        self.frame_atual = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.direcao = direcao
        self.velocidade = velocidade

        if direcao == "esquerda":
            self.rect.midleft =  (-60, 210)
        else:
            self.rect.midright = (636, 210)


    def mover(self):

        if self.direcao == "esquerda":
            self.rect.x += self.velocidade
        else:
            self.rect.x -= self.velocidade
    
    def animar(self):
        self.frame_atual += 0.25

        if self.frame_atual >= len(self.frames):
            self.frame_atual = 0
        
        self.image = self.frames[int(self.frame_atual)]

    def atualizar(self):
        self.mover()
        self.animar()

    def atingir_player(self, player):
     
        return self.rect.colliderect(player.rect)