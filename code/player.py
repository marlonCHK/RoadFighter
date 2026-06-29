import pygame

class Player:
    def __init__(self):
        #parado
        idle_sheet = pygame.image.load('./assets/Idle.png').convert_alpha()

        self.idle = idle_sheet.subsurface((0,0,128,128))

        #atacando
        attack_sheet = pygame.image.load('./assets/Attack.png').convert_alpha()
        self.attack_frames = []

        for i in range(4):
            frame = attack_sheet.subsurface((i * 128, 0, 128, 128))

            self.attack_frames.append(frame)
        
        self.image = self.idle
        self.rect = self.image.get_rect(center=(288, 210))
        self.hitbox = pygame.Rect(0,0,40,70)
        self.hitbox.center = self.rect.center
        self.attacking = False
        self.attack_direction = "direita"
        self.attack_frame = 0

    def atacar(self, direcao):

        if not self.attacking:
            self.attacking = True
            self.attack_direction = direcao
            self.attack_frame = 0

    def atualizar(self):

        if self.attacking:
            self.attack_frame += 0.20

            if self.attack_frame >= len(self.attack_frames):

                self.attacking = False
                self.image = self.idle

            else:
                frame= self.attack_frames[int(self.attack_frame)]

                if self.attack_direction == "esquerda":

                    frame = pygame.transform.flip(frame, True, False)
                    
                self.image = frame
                self.hitbox.center = self.rect.center