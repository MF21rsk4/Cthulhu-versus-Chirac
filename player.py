import pygame
import random
from projectile import Projectile
from projectile import Projectile_reversal

# CHARACTER CHARACTER CHARACTER
class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game= game
        self.health= 100
        self.max_health= 100
        self.attack= 1
        self.velocity= 7
        self.all_projectiles = pygame.sprite.Group()
        self.image= pygame.image.load('assets/monstergreen.png')
        self.image= pygame.transform.scale(self.image, (220, 290))
        self.rect = self.image.get_rect()
        self.rect.x= 600
        self.rect.y= 500
        
    def updatde_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 100, self.rect.y - 30, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 100, self.rect.y - 30, self.health, 10])
    
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
    
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        
    def launch_projectile_reversal(self):
        self.all_projectiles.add(Projectile_reversal(self))
    
    def move_right(self):
        self.rect.x += self.velocity
        
    def move_left(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x -= self.velocity
        else:
            # prend des degats
            self.game.player.damage(self.attack)
            
    def move_up(self):
        self.rect.y += self.velocity