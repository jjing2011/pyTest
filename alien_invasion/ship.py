import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """ init ship and setup the pos"""
        super().__init__()

        self.ai_settings = ai_settings
        self.screen = screen

        # load ship image and get the rect
        self.image = pygame.image.load('images/ship.bmp')
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # draw ship in the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ship pos by move flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """draw ship in the certain pos"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """center ship on screen"""
        self.center = self.screen_rect.centerx