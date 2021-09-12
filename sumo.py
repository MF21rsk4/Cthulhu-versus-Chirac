import pygame


white = (255, 255, 255)
class Sumo(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 23
        self.max_health = 10
        self.attack = 1
        self.image = pygame.image.load('assets/sumo.gif')
        self.image.convert_alpha()
        self.image.set_colorkey(white)
        self.image = pygame.transform.scale(self.image, (350, 350))
        self.velocity = 2
        self.rect = self.image.get_rect()
        self.rect.x = -900
        self.rect.y = 460
        
    def damage(self, amount):
    
        self.health -= amount
        
        if self.health <= 0:
        # respawn
            self.game.sound_manager.play('nani')
            self.rect.x = -450
            self.game.score += 2
            self.health = self.max_health
            print("dosukoi")
            
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x += self.velocity
        else:
            self.game.player.damage(self.attack)