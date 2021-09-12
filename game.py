
import pygame
from sounds import SoundManager
from player import Player
from monster import Monster
from sumo import Sumo

from comet_event import CometFallEvent



class Game:
    
    def __init__(self):
        
        # Mettre FALSE pour activer ecran d'acceuil       --> les gnous sont billingues
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.all_sumos = pygame.sprite.Group()
        self.sound_manager = SoundManager()
        self.score = 0
        self.pressed = {}
        self.comet_event = CometFallEvent(self)
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_sumo()
    
    
    def game_over(self):
        # egalement la pause + permet un quick reset
        self.all_monsters = pygame.sprite.Group()
        self.all_sumos = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.spawn_monster()
        self.spawn_monster()
        self.sound_manager.play('game_over')
        
    def stage_clear(self):
        
        self.all_monsters = pygame.sprite.Group() #choucrane choufiane
        self.all_sumos = pygame.sprite.Group()
        
        self.player.health = self.player.max_health
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.is_playing = True
        #self.score = 0
        #self.sound_manager.play('GG')
        
    #def GG(self, screen):
        #yuhane = pygame.image.load('assets/Yuhane.png')
        #yuhane = yuhane.image.get_rect()
        #yuhane.get_rect.x = 500
        #yuhane.get_rect.y = 300
        #screen.blit(yuhane, yuhane.rect)
    
    def update(self, screen):
        
        font = pygame.font.SysFont("monospace", 48)
        
        score_text = font.render(f"Kill : {self.score}", 1, (10, 187, 10))
        
        screen.blit(score_text, (20, 20))
    
        screen.blit(self.player.image, self.player.rect)
    
        self.player.updatde_health_bar(screen)
        
        self.comet_event.update_bar(screen)
    
        for projectile in self.player.all_projectiles:
            projectile.move()
        
        
        for monster in self.all_monsters:
            monster.forward()
    
        for comet in self.comet_event.all_comets:
            comet.fall()
            
        for sumo in self.all_sumos:
            sumo.forward()
    
        self.player.all_projectiles.draw(screen)
    
        self.all_monsters.draw(screen)
        
        self.all_sumos.draw(screen)
        
        self.player.all_projectiles.draw(screen)
        
        self.comet_event.all_comets.draw(screen)
    
    #PROBLEM PRESSED 
        #self.pressed[event.key] = True
        #if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + game.player.rect.width < screen.get_width() -50:
            #self.player.move_right()
        #elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            #self.player.move_left()
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
            
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
        
    def spawn_sumo(self):
        sumo = Sumo(self)
        self.all_sumos.add(sumo)
        
    #def stage_2(self):
        #if score >= 5:
            #self.all_sumos.spawn_sumo()