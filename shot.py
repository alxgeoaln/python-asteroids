import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    containers = None
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        circle = pygame.draw.circle(screen, "red", self.position, self.radius, self.radius)
        return circle
    
    def update(self, dt):
        self.position += self.velocity * dt