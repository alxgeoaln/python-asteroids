import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)    
    player = Player(x, y)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    AsteroidField()
    
    Shot.containers = (shots)
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        screen.fill("black")

        for d in drawable:
            d.draw(screen)
            
        for s in shots:
            s.draw(screen)
        
        shots.update(dt)
            
        for asteroid in asteroids:
            for s in shots:
                if(s.is_collision(asteroid)):
                    asteroid.split()
                    s.kill()
            
            is_collision = player.is_collision(asteroid)
            if(is_collision):
                print("Game over!")

        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000


if __name__ == "__main__":
    main()
