import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("autoclicker go brrrr")
clock = pygame.time.Clock()
screen.fill((255,255,255))

building = [0]

rect1 = pygame.rect.Rect((screen.get_width() / 10) * 7, (screen.get_height() / 4) - (screen.get_height() / 4 * len(building) - 1.69 * (screen.get_height() / 4) * (len(building) - 1)), screen.get_width() / 3, screen.get_height() / 6)

building.append(1)

rect2 = pygame.rect.Rect((screen.get_width() / 10) * 7, (screen.get_height() / 4) - (screen.get_height() / 4 * len(building) - 1.69 * (screen.get_height() / 4) * (len(building) - 1)), screen.get_width() / 3, screen.get_height() / 6)

building.append(2)

rect3 = pygame.rect.Rect((screen.get_width() / 10) * 7, (screen.get_height() / 4) - (screen.get_height() / 4 * len(building) - 1.69 * (screen.get_height() / 4) * (len(building) - 1)), screen.get_width() / 3, screen.get_height() / 6)


while True:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen,(255,0,0),rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)
    pygame.draw.rect(screen,(0,0,255),rect3)

    pygame.display.update()
    dt = clock.tick(60) / 1000