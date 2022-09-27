import pygame
class Ship:
    def __init__(self,ai_game) :

        self.screen= ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
    def  blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self) :
        """update the ship's position based on the movemnet flag. """


        if self.moving_right:
            
            self.rect.x += 1
