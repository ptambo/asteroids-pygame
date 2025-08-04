import os
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
import player
import circleshape
import asteroid
import asteroidfield
import shot
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #create groups for objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, updatable, drawable)
    #instantiate player
    pl = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #instantiate asteroidfield
    af = asteroidfield.AsteroidField()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.collision(pl):
                print("GAME OVER!")
                return
            for s in shots:
                if a.collision(s):
                    a.split()
                    s.kill()
        for d in drawable:
            d.draw(screen)    
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
