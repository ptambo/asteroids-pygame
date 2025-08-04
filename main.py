import os
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
import player
import circleshape
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #create 2 groups for objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    #instantiate player
    pl = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for x in updatable:
            x.update(dt)
        for x in drawable:
            x.draw(screen)    
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
