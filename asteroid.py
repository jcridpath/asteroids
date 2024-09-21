import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, asteroid_field):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        deflection = random.uniform(20, 50)
        angle_one = self.velocity.rotate(deflection)
        angle_two = self.velocity.rotate(-deflection)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_field.spawn(radius, self.position, angle_one * 1.2)
        asteroid_field.spawn(radius, self.position, angle_two * 1.2)



