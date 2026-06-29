import pygame
from code.Entity_factory import EntityFactory
from code.Player import Player

class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.ataque_distancia = 90
        self.tempo_inicial = pygame.time.get_ticks()
        self.inimigos_derrotados = 0
        
        self.background = pygame.image.load("./assets/level1bg.png").convert()
        self.background_rect = self.background.get_rect()
        
        self.som_soco = pygame.mixer.Sound("./assets/punch_2.wav")

        self.player = Player()
        self.enemy_list = []
        self.SPAWN_ENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWN_ENEMY, 1700)

    def iniciar(self):
        pygame.mixer.music.load('./assets/fight.wav')
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            #eventos
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == self.SPAWN_ENEMY:
                    velocidade = 3 + self.obter_tempo  () // 15
                    self.enemy_list.append(EntityFactory.criar_inimigo(velocidade))

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        self.player.atacar("esquerda")
                        self.atacar("esquerda")

                    if event.key == pygame.K_RIGHT:
                        self.player.atacar("direita")
                        self.atacar("direita")

            self.player.atualizar()
            
            #desenho
            self.window.blit(self.background, (0, 0))
            self.window.blit(self.player.image, self.player.rect)

            #inimigo

            if self.verificar_game_over():
                pygame.mixer.music.stop()
                return True

            for enemy in self.enemy_list[:]:
                enemy.atualizar()

                if enemy.dead:
                    self.enemy_list.remove(enemy)
                    self.inimigos_derrotados += 1
                    continue

                elif enemy.rect.right < 0 or enemy.rect.left > 576:
                    self.enemy_list.remove(enemy)
                    continue

                self.window.blit(enemy.image, enemy.rect)


            self.desenhar_hud()
            pygame.display.flip()

    def atacar(self, direcao):

        player_x = self.player.rect.centerx
        inimigos = []

        for enemy in self.enemy_list:
            if enemy.direcao != direcao:
                continue

            distancia = abs(enemy.rect.centerx - player_x)

            if distancia <= self.ataque_distancia:
                inimigos.append(enemy)

        #nao encontrou
        if not inimigos:
            return

        #Pega o mais próximo
        alvo = min(
            inimigos,
            key=lambda enemy: abs(enemy.rect.centerx - player_x)
        )

        alvo.tomar_dano()
        self.som_soco.play()

    def verificar_game_over(self):

        for enemy in self.enemy_list:

            if enemy.atingir_player(self.player):
                return True
            
        return False
    
    def obter_tempo(self):
        return (pygame.time.get_ticks() - self.tempo_inicial) // 1000

    def desenhar_hud(self):

        fonte = pygame.font.SysFont("Arial", 22)

        tempo = fonte.render(
            f"Tempo: {self.obter_tempo()} s",
            True,
            (255,255,255)
        )

        inimigos = fonte.render(
            f"Inimigos: {self.inimigos_derrotados}",
            True,
            (255,255,255)
        )

        self.window.blit(tempo, (10,10))
        self.window.blit(inimigos, (10,40))