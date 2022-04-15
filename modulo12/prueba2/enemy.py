import pygame
from constants import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        size = (20, 20)
        self.image = pygame.Surface(size)
        self.image.fill(BACKGROUND_ENEMY)

        self.rect = self.image.get_rect()

        self.rect.x = int(pos_x)
        self.rect.y = int(pos_y)

        self.speed = 3

    def down(self):
        self.rect.y += self.speed
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    