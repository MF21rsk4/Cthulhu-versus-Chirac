import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__() 
        self.velocity= 5
        self.player = player
        self.image = pygame.image.load('assets/slimeball.png')
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 110
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 1

    
class Projectile_reversal(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__() 
        self.velocity= -4
        self.player = player
        self.image = pygame.image.load('assets/slimeball.png')
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 80
        self.rect.y = player.rect.y + 160
        self.origin_image = self.image
        self.angle = 0
        
        
        
    def rotate(self):
        self.angle += 6
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        
    def remove(self):
        self.player.all_projectiles.remove(self)
        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)
            
        for sumo in self.player.game.check_collision(self, self.player.game.all_sumos):
            self.remove()
            sumo.damage(self.player.attack)
    
        # enlever les projectiles hors ecran pour optimiser
       