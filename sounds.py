import pygame

class SoundManager:
    
    def __init__(self):
        self.sounds = {'click': pygame.mixer.Sound("assets/sounds/itstime_1.ogg"),
                       'corde': pygame.mixer.Sound('assets/sounds/meteorite.ogg'),
                       'tir': pygame.mixer.Sound('assets/sounds/tir.ogg'),
                       'game_over': pygame.mixer.Sound('assets/sounds/game_over.ogg'),
                       'theme': pygame.mixer.Sound('assets/sounds/theme.ogg'),
                       'home_page': pygame.mixer.Sound('assets/sounds/home_page.ogg'),
                       'GG': pygame.mixer.Sound('assets/sounds/gg.ogg'),
                       'nani': pygame.mixer.Sound('assets/sounds/nani.ogg'),
                       'methode': pygame.mixer.Sound('assets/sounds/methode.ogg'),
                       }
        
    def play(self, name):
        self.sounds[name].play()