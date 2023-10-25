import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((700,500))
clock = pygame.time.Clock()
screen.fill("gray")

socialcredit = 0

rect = pygame.rect.Rect(screen.get_width()/2-40,screen.get_height()/2-40,80,80)

with open("../assets/phont.ttf") as file:
    font = pygame.font.Font(file,18)
    text = font.render(str(socialcredit) + " social credit",True,"white")
    textsurface = text.get_rect()
    textsurface.center = (screen.get_width()/2,screen.get_height()/2-200)

mousepos = pygame.mouse.get_pos()

while True:
    screen.fill("gray")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(pygame.mouse.get_pos()):
                socialcredit += 1


    text = font.render(str(socialcredit) + " social credit", True, "white") # i have no idea why it doesnt work it just doesnt wnat to ig

    pygame.draw.rect(screen,"black",rect)
    screen.blit(text,textsurface)
    pygame.display.update()
    dt = clock.tick(60) / 1000