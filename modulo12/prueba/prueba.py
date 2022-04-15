import pygame
import sys

pygame.init()

ventana = pygame.display.set_mode( (500, 400) )
pygame.display.set_caption("Hola Mundo")
rect = pygame.Rect(80, 100, 120, 30)

while True:
    ventana.fill( (51, 193, 255) )
    pygame.draw.rect(ventana, (141, 51, 255), rect )
    pygame.display.update()
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_a]:
        rect.x = rect.x - 1
    if tecla[pygame.K_d]:
        rect.x = rect.x + 1
    if tecla[pygame.K_w]:
        rect.y = rect.y - 1
    if tecla[pygame.K_s]:
        rect.y = rect.y + 1
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()