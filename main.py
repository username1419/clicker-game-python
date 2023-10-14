import pygame
import sys
import json
import math

class Cookie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.cookiepic = pygame.image.load('assets/cookie.png')
        self.cookiepic = pygame.Surface.convert_alpha(self.cookiepic)
        self.rect = pygame.rect.Rect(x - self.cookiepic.get_width() / 2, y - self.cookiepic.get_height() / 2, self.cookiepic.get_width(),self.cookiepic.get_height())
        self.radius = (self.rect.right - self.rect.left) / 2

        screen.blit(self.cookiepic,self.rect)
    def draw(self, surface):
        screen.blit(self.cookiepic, surface)

class Building(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface | str, name: str, starting_price: int, value: float):
        super().__init__()
        global font
        building.append(self)
        self.image = image if type(image) != str else pygame.image.load(image)
        self.name = name
        self.price = starting_price
        self.value = value
        self.amount = 0
        self.totalvalue = 0
        self.rect = pygame.rect.Rect((screen.get_width() / 10) * 7, (screen.get_height() / 4) - (screen.get_height() / 4 * len(building) - 1.69 * (screen.get_height() / 4) * (len(building) - 1)), screen.get_width() / 3, screen.get_height() / 6)
        self.textname = font.render(self.name, True, "black")
        self.textprice = font.render(str(self.price) + " cookies", True, "black")

    def increment(self):
        global kookiekount
        global text
        global textsurface
        if kookiekount >= self.price:
            self.amount += 1
            self.totalvalue = self.value * self.amount
            kookiekount -= self.price
            self.price = int(self.price * 1.1)
            self.textprice = font.render(str(self.price) + " cookies", True, "black")
            text = font.render(str(kookiekount) + " cookies", True, "white")

            if kookiekount % 10 == 0:
                textsurface = pygame.rect.Rect((screen.get_width() / 2) - (text.get_width() / 2),(screen.get_height() / 2) - (screen.get_height() / 3), text.get_width(),text.get_height())

    def draw(self):
        pygame.draw.rect(screen, "white", self.rect)
        screen.blit(self.image, self.rect)
        screen.blit(self.textname, (self.rect.topright[0] - self.textname.get_width() * 2,self.rect.topright[1] + self.textname.get_height() / 2))
        screen.blit(self.textprice, (self.rect.bottomright[0] - self.textprice.get_width() * 1.6,self.rect.bottomright[1] - self.textprice.get_height() * 2))

    def addbuilding(self,amount):
        global textsurface
        global text

        self.amount += amount
        self.totalvalue = self.value * self.amount
        for i in range(amount):
            self.price = int(self.price * 1.1)
        self.textprice = font.render(str(self.price) + " cookies", True, "black")
        text = font.render(str(kookiekount) + " cookies", True, "white")

        if kookiekount % 10 == 0:
            textsurface = pygame.rect.Rect((screen.get_width() / 2) - (text.get_width() / 2),(screen.get_height() / 2) - (screen.get_height() / 3), text.get_width(),text.get_height())


pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("cookie go click")
clock = pygame.time.Clock()

SECONDTIMER = pygame.USEREVENT + 1
pygame.time.set_timer(SECONDTIMER,1000)

queue = 0.0
building = []

with open('data/data.json') as file:
    data = json.load(file)
    kookiekount = data["kookiekount"]

font = pygame.font.Font("assets/phont.ttf",16)
text = font.render(str(kookiekount) + " cookies", True, "white")
textsurface = pygame.rect.Rect((screen.get_width() / 2) - (text.get_width() / 2), (screen.get_height() / 2) - (screen.get_height() / 3), text.get_width(), text.get_height())

cookie = Cookie((screen.get_width() / 2), (screen.get_height() / 2))
cursor = Building("assets/cursor.png","Auto-Clicker",10,0.1)
grandma = Building("assets/grandma.png","Grandma",100,1)

with open('data/data.json') as file:
    data = json.load(file)
    elements = data.keys()

    if 'cursor' in elements:
        cursor.addbuilding(data['cursor'])
    elif 'grandma' in elements:
        grandma.addbuilding(data['grandma'])

while True:
    screen.fill((122, 169, 245))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            with open('data/data.json','r+') as file:

                data = json.load(file)
                file.seek(0)
                dict = {"kookiekount":kookiekount}
                if cursor.amount > 0:
                    dict['cursor'] = cursor.amount
                if grandma.amount > 0:
                    dict['grandma'] = grandma.amount

                file.write(json.dumps(dict,indent=4))
                file.truncate()

            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mousepos = pygame.mouse.get_pos()
            xdiff = abs(mousepos[0] - cookie.rect.center[0])
            ydiff = abs(mousepos[1] - cookie.rect.center[1])

            if math.sqrt(xdiff**2 + ydiff**2) < cookie.radius:

                kookiekount += 1
                text = font.render(str(kookiekount) + " cookies", True, "white")

                if kookiekount % 10 == 0:

                    textsurface = pygame.rect.Rect((screen.get_width() / 2) - (text.get_width() / 2), (screen.get_height() / 2) - (screen.get_height() / 3), text.get_width(), text.get_height())

            elif grandma.rect.collidepoint(mousepos):
                grandma.increment()

            elif cursor.rect.collidepoint(mousepos):
                cursor.increment()

        if event.type == SECONDTIMER:
            totalvalue = 0
            for i in building:
                totalvalue += i.totalvalue
            queue += totalvalue % 1
            if queue > 0.9:
                totalvalue += int(queue)
                queue %= 1
            kookiekount += int(totalvalue)

    mousepos = pygame.mouse.get_pos()
    xdiff = abs(mousepos[0] - cookie.rect.center[0])
    ydiff = abs(mousepos[1] - cookie.rect.center[1])

    if math.sqrt(xdiff**2 + ydiff**2) < cookie.radius:

        cookie.cookiepic = pygame.transform.scale(cookie.cookiepic,(180,180))
        cookie.rect.left = screen.get_width() / 2 - cookie.cookiepic.get_width() / 2
        cookie.rect.top = screen.get_height() / 2 - cookie.cookiepic.get_height() / 2

    elif cookie.cookiepic.get_width() == 180:

        cookie.cookiepic = pygame.image.load('assets/cookie.png')
        cookie.cookiepic = pygame.Surface.convert_alpha(cookie.cookiepic)
        cookie.rect.left = screen.get_width() / 2 - cookie.cookiepic.get_width() / 2
        cookie.rect.top = screen.get_height() / 2 - cookie.cookiepic.get_height() / 2

    cookie.radius = (cookie.rect.right - cookie.rect.left) / 2

    text = font.render(str(kookiekount) + " cookies", True, "white")

    if kookiekount % 10 == 0:
        textsurface = pygame.rect.Rect((screen.get_width() / 2) - (text.get_width() / 2),(screen.get_height() / 2) - (screen.get_height() / 3), text.get_width(),text.get_height())

    cookie.draw(cookie.rect)
    screen.blit(text, textsurface)
    grandma.draw()
    cursor.draw()
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
