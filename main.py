import pygame
import math
import pygame,sys
from pygame.locals import *


from game import Game
#from option import Options
#from pygame.locals import *
from projectile import Projectile_reversal


pygame.init()
        

clock = pygame.time.Clock()
FPS = 20
  

pygame.display.set_caption("cthulhu vs chirac")
# 1080 720
screen = pygame.display.set_mode((1100, 800))


background = pygame.image.load('assets/voila.jpg')
background.convert()

troll = pygame.image.load('assets/chirac.png')
troll_rect = troll.get_rect()
troll_rect.x = 400
troll_rect.y = 200

yuhane = pygame.image.load('assets/okYUHA.JPG')
#yuhane = pygame.transform.scale(yuhane, (800, 1000)) x 100 y -10
yuhane_rect = yuhane.get_rect() 
yuhane_rect.x = 75
yuhane_rect.y = 80

banner = pygame.image.load('assets/banner.jpg')
banner = pygame.transform.scale(banner, (1200, 500))

white = (255, 255, 255)

play_button = pygame.image.load('assets/boutonjouer.png')
play_button = pygame.transform.scale(play_button, (128, 128))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.5) #2.5
play_button_rect.y = math.ceil(screen.get_height() / 1.5) #1.4

option_button = pygame.image.load('assets/option.jpg')
option_button.convert_alpha()
option_button.set_colorkey(white)
option_button = pygame.transform.scale(option_button, (190, 100))
option_button_rect = option_button.get_rect()
option_button_rect.x = math.ceil(screen.get_width() / 2.66) #6 1.5
option_button_rect.y = math.ceil(screen.get_height() / 1.22)

game = Game()

running = True

while running:
    #appliquer la fenetre, joueur, etc.
        screen.blit(background, (0, -200))
        
    # verifier debut du jeu
        if game.is_playing:
            game.update(screen)
        
        else:
            screen.blit(banner, (0, 0))
            screen.blit(play_button, play_button_rect)
            screen.blit(option_button, option_button_rect)
            
        if game.player.health <= 5:
            game.game_over()
        
        if game.score >= 17: #17
            game.stage_clear()
            screen.blit(yuhane, yuhane_rect)
            game.sound_manager.play('GG')
        
        
        if game.score == 12:
            screen.blit(troll, troll_rect)
            game.sound_manager.play('methode')
            
        if game.score == 13:
            screen.blit(troll, troll_rect)
            #game.sound_manager.play('methode')
            
            
        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width() -50:
            game.player.move_right()
        elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
            game.player.move_left()
        #elif game.pressed.get(pyagme.K_EXCLAIM) and game.player.rect.y > 400:
            #game.player.move_up()
        
    
        pygame.display.flip()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Ftagn'")
            
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
            
                if event.key == pygame.K_LCTRL:
                    
                    game.player.launch_projectile_reversal()
                    
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
                        
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                if play_button_rect.collidepoint(event.pos):
                    game.is_playing = True
                    
                    game.sound_manager.play('click')
                    game.sound_manager.play('theme')
                
                    
clock.tick(FPS)
