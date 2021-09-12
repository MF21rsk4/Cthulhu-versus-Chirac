import random
import pygame

from comet import Comet
from sounds import SoundManager


class CometFallEvent:
    # le compteur
    def __init__(self, game):
        self.sound_manager = SoundManager
        self.percent = 0
        self.percent_speed = 35
        self.game = game
        # best speed 17
        
        self.all_comets = pygame.sprite.Group()
        
    def add_percent(self):
        self.percent += self.percent_speed / 100
        #self.percent += 1
        
    def is_full_loaded(self):
        return self.percent >= 100
        
    
        
    def reset_percent(self):
        self.percent = 0
        
    def meteor_fall(self):
        self.all_comets.add(Comet(self))

    
    def attempt_fall(self):
        # jauge full
        if self.is_full_loaded():

            print("IL PLEUT DES CORDES !!!")

            for i in range(1, 4):
                self.meteor_fall()
                self.reset_percent()
    
        
    def update_bar(self, surface):
        
        self.add_percent()
        
        self.attempt_fall()
        
        pygame.draw.rect(surface, (60, 63, 60), [0, surface.get_height() - 520, 700, 10])
        # axe x, y, longueur, epaisseur
        
        pygame.draw.rect(surface, (20, 80, 187), [0, surface.get_height() - 520, (700 / 100) * self.percent, 10])
