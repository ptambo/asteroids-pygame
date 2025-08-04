import circleshape
import pygame
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
       self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #create random angle and 2 new astroids that are rotated with and against the random angle
        rndangle = random.uniform(20, 50)
        as1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        as2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        as1.velocity = self.velocity.rotate(rndangle)*1.2
        as2.velocity = self.velocity.rotate(-rndangle)*1.2