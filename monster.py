import random
import pygame


class Monster(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 13
        self.max_health = 6
        self.attack = 1
        self.image = pygame.image.load('assets/chirac.png')
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (160, 180))
        self.velocity = random.randint(1, 2)
        self.rect = self.image.get_rect()
        self.rect.x = -300
        self.rect.y = 580
        
        
    def damage(self, amount):
        self.health -= amount
        
        if self.health <= 0:
        # respawn
            self.game.sound_manager.play('tir')
            self.rect.x = -300
            self.game.score += 1
            self.health = self.max_health
            self.velocity = random.randint(3, 5)
            print('this is not a methode !')
        
               
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x += self.velocity
        else:
            self.game.player.damage(self.attack)
            
            
#class Chirac(Monster):
    
    #def __init__(self, game):
        #super().__init__(game, "chirac")
