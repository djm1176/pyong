import sys

if not __name__ == "__main__":
    print("Cannot run this file in this context")
    sys.exit(0)

import pygame
import math
import time
import gameobject
from config import *
from pygame.locals import *
from pygame import *
from graphics import Camera
from pygame.math import Vector2
from gameobject import GameObject



pygame.init()

display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Ultimate Pong")
clock = pygame.time.Clock()

fps_delay = 60
fps_delta = 0

camera = Camera()

background = GameObject(position = Vector2(0, 0), scale = Vector2(SCREENWIDTH, SCREENHEIGHT))
background.colorize(pygame.Color(255, 255, 255))

ball = GameObject(position = Vector2(40, 40))
ball.colorize(pygame.Color(255, 0, 0))

while True:
    #TODO: Move inputs into a custom class and handle with single function call
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Closing game...")
            pygame.quit()
            sys.exit(0)
            
        elif event.type == KEYDOWN:
            print("Key Down: ", event.key)
        elif event.type == KEYUP:
            print("Key Up: ", event.key)
    
    camera.render(display)
    pygame.display.update()
    clock.tick(60)
    
    if fps_delta >= fps_delay and DEBUGGING:
        fps_delta = 0
        print("%0.2f" % clock.get_fps() + " FPS")
    
    fps_delta += 1
