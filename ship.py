import pygame
class Ship:
    def __init__(self,ai_game) :


        self.screen= ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False 
    def  blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self) :
        """update the ship's position based on the movemnet flag. """
        

        if self.moving_right and self.rect.right < self.screen_rect.right:
            # update the x attribute (bcz .rect in pygame does not store decimal values)
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x