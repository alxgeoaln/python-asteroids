import pygame
import random

from circleshape import CircleShape

from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = None
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        
    def draw(self, screen):
        circle = pygame.draw.circle(screen, "white", pygame.Vector2(self.position, self.position), self.radius, 2)
        return circle
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if(self.radius <= ASTEROID_MIN_RADIUS):
            self.kill();
        
        random_angle =random.uniform(20, 50)
        first_circle = self.velocity.rotate(random_angle)
        second_circle = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid_one.velocity += first_circle * 1.2
        asteroid_two.velocity += second_circle * 1.2
        
        self.kill()
        
        
        