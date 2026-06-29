import pygame

class Inimigo:
    def __init__(self, direcao, velocidade):
        run_sheet = pygame.image.load('./assets/Run.png').convert_alpha()
        hurt_sheet = pygame.image.load('./assets/Hurt.png').convert_alpha()

        self.run_frames = []
        self.hurt_frames = []

        for i in range(10):
            frame = run_sheet.subsurface((i * 128, 0, 128, 128))

            if direcao == "direita":
                frame = pygame.transform.flip(frame, True, False)

            self.run_frames.append(frame)

        for i in range(3):

            frame = hurt_sheet.subsurface((i*128,0,128,128))

            if direcao == "direita":
                frame = pygame.transform.flip(frame, True, False)

            self.hurt_frames.append(frame)
        
        self.frame_atual = 0
        self.image = self.run_frames[0]
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(0,0,40,70)
        self.hitbox.center = self.rect.center
        self.direcao = direcao
        self.velocidade = velocidade
        self.hurt = False
        self.dead = False

        if direcao == "esquerda":
            self.rect.midleft =  (-60, 210)
        else:
            self.rect.midright = (636, 210)


    def mover(self):

        if self.direcao == "esquerda":
            self.rect.x += self.velocidade
        else:
            self.rect.x -= self.velocidade
        
        self.hitbox.center = self.rect.center
    
    def animar(self):
        if self.hurt:

            self.frame_atual += 0.25

            if self.frame_atual >= len(self.hurt_frames):

                self.dead = True

            else:
                self.image = self.hurt_frames[int(self.frame_atual)]

        else:
            self.frame_atual += 0.25

            if self.frame_atual >= len(self.run_frames):

                self.frame_atual = 0

            self.image = self.run_frames[int(self.frame_atual)]


    def atualizar(self):
        if not self.hurt:
            self.mover()

        self.animar()

    def atingir_player(self, player):
     
        return self.hitbox.colliderect(player.hitbox)
    
    def tomar_dano(self):

        if not self.hurt:
            self.hurt = True
            self.frame_atual = 0