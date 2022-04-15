import pygame
from constants import *

class Player(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        size = (40, 40)
        self.image = pygame.Surface(size)
        self.image.fill(BACKGROUND_PLAYER)

        self.rect = self.image.get_rect()

        self.rect.x = int(pos_x)
        self.rect.y = int(pos_y)

        self.speed = 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def left(self):
        self.rect.x -= self.speed

    def right(self):
        self.rect.x += self.speed

    def up(self):
        self.rect.y -= self.speed

    def down(self):
        self.rect.y += self.speed