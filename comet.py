import pygame
import random

class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('assets/corde.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = -350
        self.image = pygame.transform.scale(self.image, (200, 300))
        self.velocity = random.randint(3, 6)
        self.attack = 5
        
        self.percent = 0
        self.percent_speed = 30
        self.comet_event = comet_event
        self.all_comets = pygame.sprite.Group()
        
        
        
    def fall(self):
        self.rect.y += self.velocity
        
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.comet_event.game.player.damage(1)

        