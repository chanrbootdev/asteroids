import pygame
from constants import *
from player import *
from asteroidfield import *
import sys

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    the_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    AsteroidField()
    Shot.containers  = (shots, updatable, drawable)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0))
        for updater in updatable:
            updater.update(dt)
        for drawer in drawable:
            drawer.draw(screen)
        for aster in asteroids:
            if aster.collide(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.collide(aster):
                    bullet.kill()
                    aster.split()
        pygame.display.flip()
        dt = the_clock.tick(60)/1000

if __name__ == "__main__":
    main()
