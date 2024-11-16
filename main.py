import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Updatable Loop    
        for item in updatable:
            item.update(dt)

        screen.fill("black")

        #Drawable Loop
        for item in drawable:
            item.draw(screen)

        #Collision Loop
        for asteroid in asteroids:
            if asteroid.isCollision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.isCollision(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        # limit framrate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
