from pygame import *

SCREEN_WIGHT = 800
SCREEN_HEIGHT = 600
FPS = 60
screen = display.set_mode((800,600))
display.set_caption("Ping-Pong")

clock = time.Clock()

class GamesSprite(sprite.Sprite):
    def __init__(self, x, y, speed, wight, height, color):
        self.speed = speed
        self.color = color
        self.rect = Rect(x, y, wight, height)
    def draw(self):
        draw.rect(screen, self.color, self.rect)

player1 = GamesSprite(30, 200, 5, 30, 150, "red")
player2 = GamesSprite(740, 200, 5, 30, 150, "blue")

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
    
    player1.draw()
    player2.draw()
    display.update()
    clock.tick(FPS)

quit()from pygame import *

SCREEN_WIGHT = 800
SCREEN_HEIGHT = 600
FPS = 60
screen = display.set_mode((800,600))
display.set_caption("Ping-Pong")

clock = time.Clock()

class GamesSprite(sprite.Sprite):
    def __init__(self, x, y, speed, wight, height, color):
        self.speed = speed
        self.color = color
        self.rect = Rect(x, y, wight, height)
    def draw(self):
        draw.rect(screen, self.color, self.rect)

player1 = GamesSprite(30, 200, 5, 30, 150, "red")
player2 = GamesSprite(740, 200, 5, 30, 150, "blue")

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
    
    player1.draw()
    player2.draw()
    display.update()
    clock.tick(FPS)

quit()
