import pygame, sys

class Options:
    
    click = False

    if button_option_rect.collidepoint(event.pos):
        if click:
            option_menu()

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect) 
    
    
    def option_menu(self, screen):

        running = True
        while running:
        
            screen.fill((0, 0, 0))
            draw_text('dans les options', font, (0, 0, 255), screen, 20, 20)
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
    
    
    