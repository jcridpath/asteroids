import pygame
from pygame.locals import *
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(center_x, center_y)

    print("Player object created:", player)
    print("Player object type:", type(player))

    print(updatable)
    print(player.containers)
    dt = 0
    clock = pygame.time.Clock()
    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if player.detect_collision(asteroid):
                print("Game Over!")
                exit()
            for shot in shots:
                if asteroid.detect_collision(shot):
                    asteroid.split(asteroid_field)
                    shot.kill()

        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()

