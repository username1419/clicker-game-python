import pygame
import sys
import json

class Cookie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.cookiepic = pygame.image.load('assets/cookie.png')
        self.cookiepic = pygame.Surface.convert_alpha(self.cookiepic)
        self.rect = pygame.rect.Rect(x - self.cookiepic.get_width() / 2, y - self.cookiepic.get_height() / 2, self.cookiepic.get_width(),self.cookiepic.get_height())
        
        screen.blit(self.cookiepic,self.rect)
    def draw(self, surface):
        screen.blit(self.cookiepic, surface)

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

cookie = Cookie((screen.get_width() / 2), (screen.get_height() / 2))
with open('data/data.json') as file:
    data = json.load(file)
    kookiekount = data["kookiekount"]

font = pygame.font.Font("assets/phont.ttf",16)
text = font.render(str(kookiekount) + " cookies", True, "white")
textsurface = pygame.rect.Rect((screen.get_width() / 2) - (text.get_width() / 2), (screen.get_height() / 2) - (screen.get_height() / 3), text.get_width(), text.get_height())

while True:
    screen.fill((122, 169, 245))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('data/data.json','r+') as file:
                data = json.load(file)
                file.seek(0)
                file.write(json.dumps({"kookiekount":kookiekount},indent=4))
                file.truncate()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if cookie.rect.collidepoint(mousepos):
                kookiekount += 1
                text = font.render(str(kookiekount) + " cookies", True, "white")
                if kookiekount % 10 == 0:
                    textsurface = pygame.rect.Rect((screen.get_width() / 2) - (text.get_width() / 2), (screen.get_height() / 2) - (screen.get_height() / 3), text.get_width(), text.get_height())

    cookie.draw(cookie.rect)
    screen.blit(text, textsurface)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
