import pygame, sys

from random import randint
from constants import *
from enemy import Enemy
from player import Player

pygame.init()

surface = pygame.display.set_mode((DIMENSION))
pygame.display.set_caption('Codigo Facilito')

clock = pygame.time.Clock()

jugador = Player( WIDTH // 2, HEIGHT // 2)

enemies = pygame.sprite.Group()


while True:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_RIGHT]:
        jugador.right()

    if key_pressed[pygame.K_LEFT]:
        jugador.left()

    if key_pressed[pygame.K_UP]:
        jugador.up()

    if key_pressed[pygame.K_DOWN]:
        jugador.down()
    
    surface.fill((BACKGROUND_COLOR))

    if len(enemies) == 0:
        for number in range(0, 10):
            pos_x = randint(0, WIDTH)
            pos_y = randint(-300, -100)

            enemy = Enemy( pos_x, pos_y )
            enemies.add(enemy)

    for enemy in enemies:
        enemy.down()
        enemy.draw(surface)

        if enemy.rect.y > HEIGHT:
            enemies.remove(enemy)

        if pygame.sprite.spritecollideany(jugador, enemies):
            print('El jugador perdió')
            enemy.speed = 0
            jugador.speed = 0

    

    jugador.draw(surface)
    pygame.display.update()
