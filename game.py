if not __name__ == "__main__":
    print("Cannot run 'game.py' in this way")
    sys.exit(0)

import pygame
from pygame import *
import time
import sys

SCREENWIDTH = 960
SCREENHEIGHT = 540


pygame.init()

display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

clock = pygame.time.Clock()

fps_delay = 60
fps_delta = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Closing game...")
            pygame.quit()
            sys.exit(0)
            
        elif event.type == KEYDOWN:
            print("Key Down: ", event.key)
        elif event.type == KEYUP:
            print("Key Up: ", event.key)
    
    display.fill(pygame.Color(255, 255, 255))
    pygame.display.update()
    clock.tick(60)
    
    if fps_delta >= fps_delay:
        fps_delta = 0
        print("%0.2f" % clock.get_fps() + " FPS")
    
    fps_delta += 1
