from pygame import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
screen = display.set_mode((800,600))
display.set_caption("Ping-Pong")

clock = time.Clock()

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
    
    clock.tick(FPS)

quit()
